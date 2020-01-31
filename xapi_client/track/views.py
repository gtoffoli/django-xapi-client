import pyexcel

from xapi_client.utils import XAPI_PLATFORM
from xapi_client.utils import get_activity_choices,  get_verb_choices

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
        name = user.get_display_name()
        email = user.email
        initial = { 'name': name, 'email': email, 'endpoint': settings.LRS_ENDPOINT, 'platform': XAPI_PLATFORM }
        if recipe_ids:
            initial['recipe_ids'] = recipe_ids
        form = self.form_class(initial=initial)
        form.fields['verb_id'].choices = get_verb_choices(recipe_ids)
        form.fields['activity_type'].choices = get_activity_choices(recipe_ids)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            data = form.cleaned_data
            if form.data.get('send', ''):
                return HttpResponseRedirect('/success/')
        recipe_ids = request.POST.getlist('recipe_ids')
        if recipe_ids:
            form.fields['verb_id'].choices = get_verb_choices(recipe_ids)
            form.fields['activity_type'].choices = get_activity_choices(recipe_ids)
        return render(request, self.template_name, {'form': form})

class ImportEarmaster(View):
    form_class = ImportEarmasterForm
    template_name = 'import_earmaster.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            filename = file.name
            extension = filename.split(".")[-1]
            content = file.read()
            records = pyexcel.get_records(file_type=extension, file_content=content)
            """
            name_dict = records[0]
            keys = name_dict.keys()
            for record in records[4:]:
            """
            for record in records:
                print(record)

        return render(request, self.template_name, {'form': form})
