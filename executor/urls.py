from django.conf.urls import url
from executor import views

urlpatterns = [
    url(r'^executor/start/$', views.StartExecutor.as_view(), name = 'start executor'),
    url(r'^executor2/start/$', views.StartExecutor2.as_view(), name='start executor2'),
    # url(r'^executor/stop/$', views.StopExecutor.as_view(), name = 'stop executor'),
    # url(r'^executor/status/$', views.StatusExecutor.as_view(), name = 'status executor')
]

