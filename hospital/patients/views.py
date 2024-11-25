from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Patient, Doctor

menu = [{"title": "Специалисты", "url_name": "doctors_list"},
    {"title": "Вход", "url_name": "login"},]

def main_page(request):
    return render(request, 'patients/main_page.html', {'menu': menu, 'title': 'Главная страница'})

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'patients/doctors_list.html', {'doctors': doctors, 'title': 'Список докторов'})

def show_doctor(request, d_slug):
    doctor = get_object_or_404(Doctor, slug=d_slug)
    context = {'d': doctor, 'menu': menu}
    return render(request, 'patients/doctor.html', context = context)

def login(request):
    return render(request, 'patients/login.html', {'title': 'Логин'})

