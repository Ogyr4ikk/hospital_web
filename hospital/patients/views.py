from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Patient
menu = [{"title": "Доктора", "url_name": "doctors_list"},
    {"title": "Пациенты", "url_name": "patients_list"},
    {"title": "Вход", "url_name": "login"},]

def main_page(request):
    return render(request, 'patients/main_page.html', {'menu': menu, 'title': 'Главная страница'})
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients':patients,'title': 'Список пациентов'})
def doctors_list(request):
    return render(request, 'patients/doctors_list.html', {'title': 'Список докторов'})

def login(request):
    return render(request, 'patients/login.html', {'title': 'Логин'})

def show_patient(request, p_slug):
    patient = get_object_or_404(Patient, slug=p_slug)
    context = {'p': patient, 'menu': menu}
    return render(request, 'patients/patient.html', context = context)