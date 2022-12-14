from django.conf.urls import url
from xapi_client.track.views import SelfRecord
from xapi_client.report.views import MakeLrsQuery
from xapi_client.report.views import statements_search

urlpatterns = [
    url(r'^record/$', SelfRecord.as_view(), name='xapi_self_record'),
    url(r'^lrs_query/$', MakeLrsQuery.as_view(), name='lrs_query'),
    url(r'^lrs_search/$', statements_search, name='lrs_search'),
]
