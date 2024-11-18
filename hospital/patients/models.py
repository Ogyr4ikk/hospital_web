from django.db import models
from datetime import date

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

    def __str__(self):
        return self.last_name

