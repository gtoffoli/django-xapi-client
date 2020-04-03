from django.conf.urls import url
from xapi_client.track.views import SelfRecord
from xapi_client.report.views import MakeLrsQuery

urlpatterns = [
    url(r'^record/$', SelfRecord.as_view(), name='xapi_self_record'),
    url(r'^lrs_query/$', MakeLrsQuery.as_view(), name='lrs_query'),
]
