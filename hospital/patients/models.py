from django.db import models
from datetime import date

from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50)
    email = models.EmailField(verbose_name="e_mail", blank=True)
    birth_date = models.DateField(verbose_name="Дата рождения", default=date(2000, 1, 1))
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    is_healing = models.BooleanField(verbose_name="Лечится", default=True)
    photo = models.ImageField(verbose_name="Фото", upload_to="photos/%Y/%m/%d")
    district = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name='Район')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('patient', kwargs={'p_slug': self.slug})
class District(models.Model):
    name = models.CharField(verbose_name="Название района", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class Doctor(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50)
    email = models.EmailField(verbose_name="e_mail", blank=True)
    telephone_number = models.CharField(verbose_name="Номер телефона", max_length=50)
    birth_date = models.DateField(verbose_name="Дата рождения", default=date(2000, 1, 1))
    speciality = models.CharField(verbose_name="Специальность", max_length=50)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    is_resting = models.BooleanField(verbose_name="В отпуске", default=False)
    photo = models.ImageField(verbose_name="Фото", upload_to="photos/%Y/%m/%d")
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'p_slug': self.slug})