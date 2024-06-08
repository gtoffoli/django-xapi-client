# This module is still too dependent on being originated by CommonSpaces!
# ASAP it should be made more generic.

import sys, os
import json
from multiprocessing import Process, Queue

from tincan import (
    RemoteLRS,
    Statement,
    Agent, AgentAccount,
    Verb,
    Activity,
    Context,
    Result,
    LanguageMap,
    ActivityDefinition,
    StateDocument,
)

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from xapi_client.utils import get_current_language
from xapi_client.utils import xapi_activities, xapi_verbs
# aliases were introduced for compatibility with CommonSpaces
from xapi_client.utils import XAPI_ACTIVITY_ALIASES, XAPI_VERB_ALIASES
try:
    XAPI_PLATFORM = settings.XAPI_DEFAULT_PLATFORM
except:
    XAPI_PLATFORM = 'unspecified platform'
XAPI_LANGUAGE = settings.LANGUAGE_CODE

EXTENDED = False

import logging
logger = logging.getLogger('tracking')

def get_name(obj):
    return hasattr(obj, '__str__') and obj.__str__() or ''

def get_description(obj):
    description = ''
    if hasattr(obj, 'description'):
        description = obj.description
    if hasattr(obj, 'short'):
        description = obj.short
    return description

def get_language(obj):
    original_language = hasattr(obj, 'original_language') and obj.original_language or None;
    current_language = get_current_language()
    if original_language:
        if current_language == original_language:
            return original_language
    return original_language or current_language

def get_object_id(request, object):
    action = object and object.__class__.__name__ or None
    if hasattr(object, 'absolute_url'):
        location = object.absolute_url()
    elif hasattr(object, 'get_absolute_url'):
        location = object.get_absolute_url()
    else:
        location = '/%s/%d/' % (action, object.id)
    if request:
        object_id = request.build_absolute_uri(location)
    elif not location.count('http'):
        object_id = '%s://%s%s' % (settings.PROTOCOL, settings.HOST, location)
    object_id = object_id.replace('cs.up2university.eu', 'www.commonspaces.eu')
    return object_id

def get_context_parent(request, target):
    target_type = target.__class__.__name__
    target_type = XAPI_ACTIVITY_ALIASES.get(target_type, target_type) # for compatibility with CommonSpaces
    return {
       'objectType': 'Activity',
       'id': get_object_id(request, target),
       'definition': {'type': xapi_activities[target_type]['type'], 'name': {'en': get_name(target)}}
    }

def get_context_grouping(request, target):
    target_type = target.__class__.__name__
    target_type = XAPI_ACTIVITY_ALIASES.get(target_type, target_type) # for compatibility with CommonSpaces
    return {
       'objectType': 'Activity',
       'id': get_object_id(request, target),
       'definition': {'type': xapi_activities[target_type]['type'], 'name': {get_language(target): get_name(target)}}
    }

def make_lrs(extended=False):
    try:
        version = settings.LRS_VERSION
        endpoint = settings.LRS_ENDPOINT
        if extended:
            endpoint = endpoint.replace('std', 'ext')
     
        if settings.LRS_USERNAME and settings.LRS_PASSWORD:
            lrs = RemoteLRS(
                version = version,
                endpoint = endpoint,
                username = settings.LRS_USERNAME,
                password = settings.LRS_PASSWORD
            )
        else:
            lrs = RemoteLRS(
                version = version,
                endpoint = endpoint,
                auth = settings.LRS_AUTH,
            )
    except Exception as e:
        logger.debug('make_lrs exception', str(e))
    return lrs

PUT_TIMEOUT = 3 # seconds; was 1

# def put_statement(request, user, verb, object, target, language=XAPI_LANGUAGE, timeout=1):
def put_statement(request, user, verb, object, target, activity_id='', result=None, response=None, score=None, language=XAPI_LANGUAGE, timeout=PUT_TIMEOUT):
    # IMPORTANT: do not confound the result argument of put_statement with local variables with same name in this module!
    # construct the actor of the statement
    # IMPORTANT - account is OK but cannot coexist with mbox or other way of uniquely identifying the actor
    try:
        actor = Agent(
            name=user.get_display_name(),
            mbox='mailto:%s' % user.email,
            # account=AgentAccount(name=str(user.pk), home_page='https://www.commonspaces.eu')
        )
    except Exception as e:
        logger.debug('put_statement exception', e)
        return False

    # construct the verb of the statement
    verb = XAPI_VERB_ALIASES.get(verb, verb) # for compatibility with CommonSpaces
    verb = Verb(
        id=xapi_verbs[verb]['id'],
        display=LanguageMap(**xapi_verbs[verb]['display']),
    )

    if object:
        # construct the object of the statement for a specific object/activity
        action = object.__class__.__name__
        action = XAPI_ACTIVITY_ALIASES.get(action, action) # for compatibility with CommonSpaces
        activity_type = xapi_activities[action]['type']
        object_id = get_object_id(request, object) # 190307 GT: defined get_object_id
        object_name = get_name(object) # 190307 GT: defined get_name
        object_description = get_description(object)
        object_language = get_language(object)
        activity_definition = ActivityDefinition(
             name=LanguageMap(**{object_language: object_name}),
             description=object_description and LanguageMap(**{object_language: object_description}) or None,
             type=activity_type,                                        
        )
        object = Activity(
            id=object_id,
            definition=activity_definition,
        )
    elif activity_id:
        # construct the object of the statement for a class of activities
        activity = xapi_activities[activity_id]
        name = LanguageMap(**activity['display'])
        description=activity.get('description', None)
        description = description and LanguageMap(**description) or None
        activity_definition = ActivityDefinition(
             name=name,
             description=description,
             type=activity['type'],                                        
        )
        object = Activity(
            id=request.build_absolute_uri(),
            definition=activity_definition,
        )

    context = {'platform': XAPI_PLATFORM, 'language': get_current_language()}
    """ 190308 GT: would produce the exception "Object of type 'UUID' is not JSON serializable" in getting the response
    if request:
        context['registration'] = str(get_registration(request))
    """
    if target:
        target_type = target.__class__.__name__
        context_activities = {}
        if target_type in ['Folder', 'Forum', 'LearningPath']:
            context_activities['parent'] = {
               'objectType': 'Activity',
               'id': get_object_id(request, target),
               'definition': {'type': xapi_activities[XAPI_ACTIVITY_ALIASES.get(target_type, target_type)]['type'], 'name': {'en': get_name(target)}}
            }
            if target_type == 'Folder':
                project = target.get_project()
                if project:
                    context_activities['grouping'] = get_context_grouping(request, project)
            elif target_type == 'Forum':
                project = target.get_project()
                if project:
                    context_activities['grouping'] = get_context_grouping(request, project)
            elif target_type == 'LearningPath':
                if target.project:
                    context_activities['grouping'] = get_context_grouping(request, target.project)
        elif target_type == 'Project':
            context_activities['grouping'] = get_context_grouping(request, target)
        if context_activities:
            context['context_activities'] = context_activities
    context = Context(**context)

    if response:
        result = Result(
            response=response,
        )

    # construct the actual statement
    statement = Statement(
        actor=actor,
        verb=verb,
        object=object,
        context=context,
        result=result,
    )
    return send_statement(statement, timeout=timeout)

# def send_statement_without_timeout(statement, success, result):
def send_statement_without_timeout(queue):
    """
    # avoid [Errno 5] Input/output error in action_process.start() .. sys.stderr.flush()
    if settings.DEBUG:
        sys.stderr = open(os.path.join(settings.BASE_DIR, 'logs', 'error.log'), 'a')
    else:
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
    """
    # construct an LRS
    lrs = make_lrs()
    statement = queue.get()
    result = queue.get()
    success = queue.get()
    # save our statement to the remote_lrs and store the response in 'response'
    try:
        lrs_response = lrs.save_statement(statement)
    except Exception as e:
        logger.debug('send_statement_without_timeout exception', e)
        lrs_response = None
    if lrs_response:
        if lrs_response.success:
            result = lrs_response.data
            success = True
            """
            try:
                # retrieve our statement from the remote_lrs using the id returned in the response
                lrs_response = lrs.retrieve_statement(lrs_response.content.id)
                if lrs_response.success:
                    result = lrs_response.content
                    success = True
                else:
                    result = lrs_response.data
                    success = False
            except Exception as e:
                result = e
            """
        else:
            result = lrs_response.data
            logger.debug(result)
    queue.put(result)
    queue.put(success)

def send_statement(statement, timeout=1):
    success = False
    result = ''
    # We create a Process
    queue = Queue()
    queue.put(statement)
    queue.put(result)
    queue.put(success)
    # action_process = Process(target=send_statement_without_timeout, args=(queue,))
    action_process = Process(daemon=True, target=send_statement_without_timeout, args=(queue,))
    try:
        # We start the process and we block for timeout seconds.
        action_process.start()
        action_process.join(timeout=timeout)
        # We terminate the process.
        if action_process.is_alive():
            action_process.terminate()
            logger.debug('send_statement timeout (', timeout, ') expired')
            return success
        result = queue.get()
        success = queue.get()
        # action_process.terminate()
    except Exception as e:
        logger.debug('send_statement exception', str(e))
    return success

def get_statement(statement_id):
    lrs = make_lrs()
    lrs_response = lrs.retrieve_statement(statement_id)
    if lrs_response.success:
        return lrs_response.success, lrs_response.content
    else:
        return lrs_response.success, ''

def get_statements(query, extended=False):
    lrs = make_lrs(extended=extended)
    filters = {}
    if query.get('since', None):
        since_iso = query['since'].isoformat()
        if extended:
            filters['data->stored'] = {'$gte': since_iso}
            del query['since']
        else:
            query['since'] = since_iso
    if query.get('until', None):
        until_iso = query['until'].isoformat()
        if extended:
            filters['data->timestamp'] = {'$lte': until_iso}
            del query['until']
        else:
            query['until'] = until_iso
    if query.get('verb', None):
        verb = query['verb']
        verb_id = xapi_verbs[verb]['id']
        if extended:
            filters['data->verb->id'] = verb_id
            del query['verb']
        else:
            query['verb'] = Verb(id=verb_id)
    if query.get('activity_type', None):
        if extended:
            activity_type = query['activity_type']
            filters['data->object->definition->type'] = xapi_activities[activity_type]['type']
            del query['activity_type']
    if query.get('activity', None):
        object_id = query['activity']
        if extended:
            filters['data->object->id'] = query['activity']
            del query['activity']
        else:
            query['activity'] = Activity(id=object_id)
    if query.get('user', None):
        mbox = 'mailto:%s' % query['user'].email
        if extended:
            filters['data->actor->mbox'] = mbox
        else:
            query['agent']  = Agent(mbox=mbox)
        del query['user']
    if query.get('platform', None):
        if extended:
            filters['data->context->platform'] = query['platform']
        del query['platform']
    if filters:
        query['filters'] = filters
    logger.debug('------------ query', query)
    if extended:
        lrs_response = lrs.query_statements({}, content=json.dumps(query))
    else:
        lrs_response = lrs.query_statements(query)
    success = lrs_response.success
    if success:
        if extended:
            statements = json.loads(lrs_response.data)['data']
        else:
            statements = json.loads(lrs_response.data)['statements']
    else:
        statements = []
    return success, statements

