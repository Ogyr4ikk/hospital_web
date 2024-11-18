from django.template.context_processors import static
from django.urls import path

from hospital import settings
from .views import *
urlpatterns = [
 path('', index, name='home'),
 path('about/', about, name='about'),
 path('patients/', patients, name='patients'),
 path('doctors/', doctors, name='teachers'),
 path('login/', login, name='login'),
]
