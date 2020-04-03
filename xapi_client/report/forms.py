from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.conf import settings

PLATFORM_CHOICES = [
    ('any', _('any')),
    ('Moodle', 'Moodle'),
    ('CommonS Platform', 'CommonSpaces'),
    ('Jupyter', 'SWAN'),
    ('EarMaster', 'EarMaster'),
]

dateTimeOptions = {
'minView': 2,
'maxView': 3,
'startView': 2,
'weekStart': 1,
'format': 'dd/mm/yyyy',
'startDate': '01/01/2020',
'endDate': '01/01/2021',
}

class LrsQueryForm(forms.Form):
    platform = forms.ChoiceField(required=False, choices=PLATFORM_CHOICES, label=_('learning platform'), widget=forms.Select(attrs={'class':'form-control'}))
    date_from = forms.DateField(required=False, label=_('date from'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'date_from', 'class':'form-control',}), help_text=_('start day, included; format: dd/mm/yyyy'))
    date_to = forms.DateField(required=False, label=_('date to'), input_formats=['%d/%m/%Y'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'date_to', 'class':'form-control',}), help_text=_('end day, excluded; format: dd/mm/yyyy'))
    courses = forms.CharField(required=False, label=_(u"Courses / Projects"), widget=forms.Textarea(attrs={'class':'form-control','rows': '2', 'cols':'80'}), help_text=_('empty field = no filter on courses / projects'))
    actors = forms.CharField(required=False, label=_(u"Actors"), widget=forms.Textarea(attrs={'class':'form-control','rows': '2', 'cols':'80'}), help_text=_('empty field = no filter on actors'))
