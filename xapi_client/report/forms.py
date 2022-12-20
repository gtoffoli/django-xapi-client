from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.conf import settings
from django.contrib.auth.models import User
from dal import autocomplete

from xapi_client.xapi_vocabularies import xapi_verbs, xapi_activities

PLATFORM_CHOICES = [
    # ('any', _('any')),
    ('CommonS Platform', 'CommonSpaces'),
    ('Moodle', 'Moodle'),
    ('Jupyter', 'SWAN'),
    ('CS devel', 'CS devel'),
    # ('EarMaster', 'EarMaster'),
]

VERB_CHOICES = [(verb, verb) for verb in sorted(list(xapi_verbs.keys()))]
ACTIVITY_CHOICES = [(act, act) for act in sorted(list(xapi_activities.keys()))]

dateTimeOptions = {
'minView': 2,
'maxView': 3,
'startView': 2,
'weekStart': 1,
'format': 'dd/mm/yyyy',
'startDate': '01/01/2020',
'endDate': '01/01/2030',
}

class LrsQueryForm(forms.Form):
    platform = forms.ChoiceField(required=False, choices=PLATFORM_CHOICES, label=_('learning platform'), widget=forms.Select(attrs={'class':'form-control'}))
    date_from = forms.DateField(required=False, label=_('date from'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'date_from', 'class':'form-control',}), help_text=_('start day, included; format: dd/mm/yyyy'))
    date_to = forms.DateField(required=False, label=_('date to'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'date_to', 'class':'form-control',}), help_text=_('end day, excluded; format: dd/mm/yyyy'))
    courses = forms.CharField(required=False, label=_("Courses / Projects"), widget=forms.Textarea(attrs={'class':'form-control','rows': '2', 'cols':'80'}), help_text=_('empty field = no filter on courses / projects'))
    actors = forms.CharField(required=False, label=_("Actors"), widget=forms.Textarea(attrs={'class':'form-control','rows': '2', 'cols':'80'}), help_text=_('empty field = no filter on actors'))

class FilterStatementsForm(forms.Form):
    platforms = forms.MultipleChoiceField(required=False, choices=PLATFORM_CHOICES, label=_('learning platform'), widget=forms.SelectMultiple(attrs={'class':'form-control', 'size': 3,}))
    since = forms.DateField(required=False, label=_('since'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'since', 'class':'form-control',}), help_text=_('start day, included; format: dd/mm/yyyy'))
    until = forms.DateField(required=False, label=_('until'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'until', 'class':'form-control',}), help_text=_('end day, excluded; format: dd/mm/yyyy'))
    user = forms.ModelChoiceField(required=False, label=_("actor"), queryset=User.objects.filter(is_active=True), widget=autocomplete.ModelSelect2(url='/user-fullname-autocomplete/'))
    verbs = forms.MultipleChoiceField(required=False, choices=VERB_CHOICES, label=_('verbs'), widget=forms.SelectMultiple(attrs={'class':'form-control', 'size': 6,}))
    activity_types = forms.MultipleChoiceField(required=False, label=_('activity types'), choices=ACTIVITY_CHOICES, widget=forms.SelectMultiple(attrs={'class':'form-control', 'size': 6,}))
