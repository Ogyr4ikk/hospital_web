# Generated by Django 5.1.3 on 2024-11-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_district_options_alter_patient_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='URL'),
        ),
    ]