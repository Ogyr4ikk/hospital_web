from django.http import HttpResponse
from django.shortcuts import render
from .models import Patient
menu = [
 {'title': "О сайте", 'url_name': 'about'},
 {'title': "Студенты", 'url_name': 'patients'},
 {'title': "Преподаватели", 'url_name': 'doctors'},
 {'title': "Войти", 'url_name': 'login'}
]
def about(request):
 return render(request, 'students/about.html', {'menu': menu, 'title': 'О сайте'})

def patients(request):
 return HttpResponse("Пациенты")

def doctors(request):
 return HttpResponse("Доктора")

def login(request):
 return HttpResponse("Авторизация")

def diagnoses(request):
    return("Диагнозы")
def index(request):
    patients = Patient.objects.all()
    context = {'patients': patients, 'menu': menu, 'title': 'Главная страница'}
    return render(request, 'students/index.html', context=context)