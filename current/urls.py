from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = 'current'

urlpatterns = [
    path('',views.index,name='index'),
    path('(?P<event_id>[0-9]+)/',views.details,name='details'),

]
