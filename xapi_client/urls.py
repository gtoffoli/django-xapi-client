from django.conf.urls import url
from xapi_client.track.views import SelfRecord

urlpatterns = [
    url(r'^record/$', SelfRecord.as_view(), name='xapi_self_record'),
]
