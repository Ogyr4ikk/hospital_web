from django.template.context_processors import static
from django.urls import path

from hospital import settings
from .views import *
urlpatterns = [
 path('', main_page, name='main_page'),
 path('doctors_list/', doctors_list, name ='doctors_list'),
 path('login/', login, name='login'),
 path('doctor/<slug:d_slug>/', show_doctor, name='show_doctor'),
]
