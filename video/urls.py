from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start_collect/$', views.CollectorStart.as_view()),
]