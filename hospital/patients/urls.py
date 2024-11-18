from django.template.context_processors import static
from django.urls import path

from hospital import settings
from .views import *
urlpatterns = [
 path('', main_page, name='main_page'),
 path('patients_list/', patients_list, name='patients_list'),
 path('doctors_list/', doctors_list, name ='doctors_list'),
 path('login/', login, name='login'),
 path('patient/<slug:p_slug>/', show_patient, name='show_patient'),
]
