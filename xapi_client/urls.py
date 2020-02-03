from django.conf.urls import url
from xapi_client.track.views import SelfRecord, ImportEarmaster

urlpatterns = [
    url(r'^record/$', SelfRecord.as_view(), name='xapi_self_record'),
    url(r'^import_earmaster/$', ImportEarmaster.as_view(), name='xapi_import_earmaster'),
]
