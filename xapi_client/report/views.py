import json
import urllib
from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required

DASHBOARD_BASE = "https://lrs.up2university.eu/dashboards/5d9f2cc11a822211045c5e75/5db710cdb8b0531954f1202c/Shareable"

from .forms import LrsQueryForm

today = datetime.now().date()
tomorrow = today + timedelta(days=1)
date_time_formats = ['%d/%m/%Y', '%d-%m-%Y',]
object_types = ['course', 'actor',]
connectives = ['and', 'or']

def get_date_time(date_time_string):
    date_time = None
    for date_time_format in date_time_formats:
        try:
            date_time = datetime.strptime(date_time_string, date_time_format)
        except ValueError:
            pass
        if date_time:
            break
    return date_time

def text_to_list(text):
    if not text:
        return []
    item_list = text.splitlines()
    item_list = [item.strip() for item in item_list]
    return [item for item in item_list if len(item)]

def parse_list(text, object_type):
    line_list = text_to_list(text)
    clauses = []
    i = 0
    for line in line_list:
        value = line.strip().lower()
        if not value:
            continue
        i += 1
        if object_type == 'course':
            value = value.replace('cs.up2university.eu', 'www.commonspaces.eu')
            value = value.replace('/en/', '/').replace('/it/', '/').replace('/pt/', '/')
            clause = {"relatedActivities":value}
            clauses.append(clause)
        elif object_type == 'actor':
            pass
    if clauses:
        return {"$or": clauses}

@method_decorator(login_required, name='post')
class MakeLrsQuery(View):
    form_class = LrsQueryForm
    template_name = 'lrs_query.html'

    def get(self, request, *args, **kwargs):
        initial = {'date_from': today, 'date_to': tomorrow,}
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        result = 'Something went wrong'
        form = self.form_class(request.POST)
        date_from = request.POST.get('date_from', '')
        date_to = request.POST.get('date_to', '')
        date_time_from = get_date_time(date_from)
        date_time_to = get_date_time(date_to)
        and_clauses = []
        if form.is_valid():
            data = form.cleaned_data
            platform = data['platform'] != 'any' and data['platform'] 
            if platform:
                platform_clause = {"statement.context.platform":platform}
                and_clauses.append(platform_clause)
            from_clause = {"$gt":{"$dte":date_time_from.isoformat().replace('00:00:00', '00:00Z')}}
            to_clause = {"$lt":{"$dte":date_time_to.isoformat().replace('00:00:00', '00:00Z')}}
            date_clause = from_clause
            date_clause.update(to_clause)
            and_clauses.append({"timestamp":date_clause})
            courses = data['courses']
            if courses:
                courses_clause = parse_list(courses, 'course')
                if courses_clause:
                    and_clauses.append(courses_clause)
            actors = data['actors']
            if actors:
                actors_clause = parse_list(actors, 'actor')
                if actors_clause:
                    and_clauses.append(actors_clause)
            plain_filter = json.dumps({"$and":and_clauses})
            print(plain_filter)
            encoded_filter = urllib.parse.quote(plain_filter)
            result = '{}?filter={}'.format(DASHBOARD_BASE, encoded_filter)
        return render(request, self.template_name, {'form': form, 'result': result})
