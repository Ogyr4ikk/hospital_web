from django.contrib import admin
from .models import Patient, District

class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'created_at', 'is_healing', 'photo', 'slug')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')
    list_editable = ('is_healing', 'slug', 'first_name')
    list_filter = ('is_healing', 'created_at')
    prepopulated_fields = {"slug": ("first_name",)}

admin.site.register(Patient, PatientsAdmin)
admin.site.register(District)