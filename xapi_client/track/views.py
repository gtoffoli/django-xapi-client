from datetime import datetime
import hashlib
import pyexcel

from tincan import (
    Statement,
    Agent,
    Verb,
    Activity,
    Context,
    LanguageMap,
    ActivityDefinition,
)

from xapi_client.utils import XAPI_PLATFORM
from xapi_client.utils import get_activity_choices,  get_verb_choices, make_uri
from xapi_client.xapi_vocabularies import xapi_verbs_by_id, xapi_activities_by_type
from xapi_client.track.xapi_statements import send_statement

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import SelfRecordForm, ImportEarmasterForm

@method_decorator(login_required, name='post')
class SelfRecord(View):
    form_class = SelfRecordForm
    template_name = 'self_record.html'

    def get(self, request, *args, **kwargs):
        try:
            recipe_ids = settings.XAPI_DEFAULT_RECIPES
        except:
            recipe_ids = []
        user = request.user
        actor_name = user.get_display_name()
        actor_email = user.email
        initial = { 'actor_name': actor_name, 'actor_email': actor_email, 'endpoint': settings.LRS_ENDPOINT, 'platform': XAPI_PLATFORM, 'authority_name': actor_name, 'authority_email': actor_email, }
        if recipe_ids:
            initial['recipe_ids'] = recipe_ids
        form = self.form_class(initial=initial)
        form.fields['verb_id'].choices = get_verb_choices(recipe_ids)
        form.fields['activity_type'].choices = get_activity_choices(recipe_ids)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        result = None
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            data = form.cleaned_data
            if form.data.get('send', ''):
                actor = Agent(
                    name=data['actor_name'],
                    mbox='mailto:{}'.format(data['actor_email'])
                )
                verb_id = data['verb_id']
                verb = Verb(
                    id=verb_id,
                    display=LanguageMap(**xapi_verbs_by_id[verb_id]['display']),
                )
                object_language = data['object_language']
                activity_definition = ActivityDefinition(
                     name=LanguageMap(**{object_language: data['object_name']}),
                     type=data['activity_type'],                                        
                )
                if data['object_description']:
                    activity_definition.description = LanguageMap(**{object_language: data['object_description']})
                object = Activity(
                    # id='http://cs.eu/{}'.format(hashlib.md5(data['object_id'].encode())),
                    id=make_uri(data['object_id']),
                    definition=activity_definition,
                )
                context = {'platform': data['platform']}
                if data['context_object_name'] and data['context_object_id']:
                    context_activity_definition = ActivityDefinition(
                        name=LanguageMap(**{object_language: data['context_object_name']}),
                        type=data['context_activity_type'],                                        
                    )
                    context_activity_object = Activity(
                        id=make_uri(data['context_object_id']),
                        definition=context_activity_definition,
                    )
                    context_activities = {
                        data['context_activity_relationship']: context_activity_object
                    }
                    context['context_activities'] = context_activities
                authority = Agent(
                    name=data['authority_name'],
                    mbox='mailto:{}'.format(data['authority_email'])
                )
                statement = Statement(
                    actor=actor,
                    verb=verb,
                    object=object,
                    context=context,
                    authority=authority,
                )
                # statement.stored = datetime.now()
                result = send_statement(statement)
        recipe_ids = request.POST.getlist('recipe_ids')
        if recipe_ids:
            form.fields['verb_id'].choices = get_verb_choices(recipe_ids)
            form.fields['activity_type'].choices = get_activity_choices(recipe_ids)
        return render(request, self.template_name, {'form': form, 'result': result})

class ImportEarmaster(View):
    form_class = ImportEarmasterForm
    template_name = 'import_earmaster.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        name = user.get_display_name()
        email = user.email
        platform = 'EarMaster'
        initial = { 'name': name, 'email': email, 'endpoint': settings.LRS_ENDPOINT, 'platform': platform }
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            filename = file.name
            print('filename:', filename)
            extension = filename.split(".")[-1]
            content = file.read()
            records = pyexcel.get_records(file_type=extension, file_content=content)
            name_dict = records[0]
            keys = name_dict.keys()
            rows = []
            for record in records:
                row = [record[key] for key in keys]
                print(row)
                rows.append(row)
        return render(request, self.template_name, {'keys': keys, 'rows': rows, 'form': form})
