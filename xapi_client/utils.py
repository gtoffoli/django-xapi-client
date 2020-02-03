from importlib import import_module

from django.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

vocabulary_module = None
try:
    vocabulary_module = import_module(settings.XAPI_VOCABULARIES_MODULE)
    xapi_verbs = getattr(vocabulary_module, 'xapi_verbs')
    xapi_activities = getattr(vocabulary_module, 'xapi_activities')
    xapi_recipes = getattr(vocabulary_module, 'xapi_recipes')
except:
    pass
if not vocabulary_module:
    from xapi_client.xapi_vocabularies import xapi_activities, xapi_verbs, xapi_recipes, xapi_contextual_activities
try:
    XAPI_PLATFORM = settings.XAPI_DEFAULT_PLATFORM
except:
    XAPI_PLATFORM = 'unspecified platform'
try:
    XAPI_ACTIVITY_ALIASES = settings.XAPI_ACTIVITY_ALIASES
except:
    XAPI_ACTIVITY_ALIASES = {}
try:
    XAPI_VERB_ALIASES = settings.XAPI_VERB_ALIASES
except:
    XAPI_VERB_ALIASES = {}
XAPI_LANGUAGE = settings.LANGUAGE_CODE

try:
    from datatrans.utils import get_current_language
except:
    from django.utils import translation

    def get_default_language():
        """
        Get the source language code if specified, else just the default language code.
        """
        lang = getattr(settings, 'SOURCE_LANGUAGE_CODE', settings.LANGUAGE_CODE)
        default = [l[0] for l in settings.LANGUAGES if l[0] == lang]
        if len(default) == 0:
            # when not found, take first part ('en' instead of 'en-us')
            lang = lang.split('-')[0]
            default = [l[0] for l in settings.LANGUAGES if l[0] == lang]
        if len(default) == 0:
            raise ImproperlyConfigured("The [SOURCE_]LANGUAGE_CODE '%s' is not found in your LANGUAGES setting." % lang)
        return default[0]

    def get_current_language():
        """
        Get the current language
        """
        lang = translation.get_language() or 'en'
        current = [l[0] for l in settings.LANGUAGES if l[0] == lang]
        if len(current) == 0:
            lang = lang.split('-')[0]
            current = [l[0] for l in settings.LANGUAGES if l[0] == lang]
        if len(current) == 0:
            # Fallback to default language code
            return get_default_language()
        return current[0]

current_language = get_current_language()[:2]


def get_activity_items(recipe_ids=None):
    if recipe_ids:
        activity_items = []
        ids = []
        for recipe_id in recipe_ids:
            recipe = xapi_recipes[recipe_id]
            activity_ids = recipe['activity_types']
            for activity_id in activity_ids:
                if not activity_id in ids:
                    activity_items.append([activity_id, xapi_activities[activity_id]])
                    ids.append(activity_id)
    else:
        activity_items = xapi_activities.items()
    return activity_items

def get_activity_choices(recipe_ids=None):
    activity_items = get_activity_items(recipe_ids=recipe_ids)
    activity_choices = []
    for key, value in activity_items:
        name = key
        activity_type = value['type']
        for language_code, activity_display in value.get('display', {}).items():
            if language_code[:2] == current_language:
                name = activity_display
                break
        activity_choices.append([activity_type, name])
    return activity_choices

def get_verb_items(recipe_ids=None):
    if recipe_ids:
        verb_items = []
        ids = []
        for recipe_id in recipe_ids:
            recipe = xapi_recipes[recipe_id]
            verb_ids = recipe['verbs']
            for verb_id in verb_ids:
                if not verb_id in ids:
                    verb_items.append([verb_id, xapi_verbs[verb_id]])
                    ids.append(verb_id)
    else:
        verb_items = xapi_verbs.items()
    return verb_items

def get_verb_choices(recipe_ids=None):
    verb_items = get_verb_items(recipe_ids=recipe_ids)
    verb_choices = []
    for key, value in verb_items:
        name = key
        verb_id = value['id']
        for language_code, verb_display in value.get('display', {}).items():
            if language_code[:2] == current_language:
                name = verb_display
                break
        verb_choices.append([verb_id, name])  
    return verb_choices

def get_recipe_choices():
    return [[key, key] for key in xapi_recipes.keys()]

def get_contextual_activity_choices():
    contextual_activity_choices = []
    for key in xapi_contextual_activities:
        name = key
        value = xapi_activities[key]
        activity_type = value['type']
        for language_code, activity_display in value.get('display', {}).items():
            if language_code[:2] == current_language:
                name = activity_display
                break
        contextual_activity_choices.append([activity_type, name])
    return contextual_activity_choices

def make_uri(text):  
    # return 'http://cs.eu/{}'.format(hashlib.md5(text.encode()).digest())
    validate = URLValidator()
    try:
        validate(text)
        return text
    except ValidationError:
        out = ''
        for c in text:
            if not c.isalnum() and not c in '-._~':
                c = '_'
            out += c
        return 'http://cs.eu/{}'.format(out)
