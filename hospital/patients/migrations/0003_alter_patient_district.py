# Generated by Django 5.1.3 on 2024-11-18 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_district_patient_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.district', verbose_name='Район'),
        ),
    ]
