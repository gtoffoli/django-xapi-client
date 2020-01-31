from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django import forms

from xapi_client.utils import get_recipe_choices, get_verb_choices, get_activity_choices

class SelfRecordForm(forms.Form):
    name = forms.CharField(required=False, label=_('full name'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('this is a computed value'),)
    email = forms.EmailField(required=False, label=_('mailbox'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('this is a computed value'),)
    platform = forms.CharField(required=False, label=_('learning platform'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('could be any activity provider'),)
    endpoint = forms.CharField(required=False, label=_('LRS endpoint'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control'}), help_text=_('this is a fixed URL'),)
    recipe_ids = forms.MultipleChoiceField(required=True, label=_('xAPI recipes'), choices=get_recipe_choices(), widget=forms.SelectMultiple(attrs={'class':'form-control', 'onchange': 'javascript: this.form.submit()',}), help_text=_('select one or more'),)
    verb_id = forms.ChoiceField(required=False, label=_('verb'), choices=get_verb_choices(), widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, choose after selecting the recipe(s); currently the match with activity type is not checked'),)
    activity_type = forms.ChoiceField(required=False, label=_('activity type'), choices=get_activity_choices(), widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, choose after selecting the recipe(s); currently the match with verb is not checked'),)
    activity = forms.CharField(required=True, label=_('activity unique identifier'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('could be a URL, a URI, a DOI, an ISBN code or the like'),)
    description = forms.CharField(required=True, label=_('activity description'), widget=forms.Textarea(attrs={'class':'form-control', 'rows': 2, }), help_text=_('a short but specific and informative description; shlould include at least a title'),)
    grouping = forms.CharField(required=False, label=_('grouping context'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('generic context, typically the unique identifier of a reference activity'),)
    parent = forms.CharField(required=False, label=_('parent context'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('typically the unique identifier of a subsuming activity; please, choose the most specific one, if any'),)
    
class ImportEarmasterForm(forms.Form):
    file = forms.FileField(label=_('select a file'), widget=forms.FileInput(attrs={'class': 'btn btn-default',}))
