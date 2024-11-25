from django import forms

class AddDoctorForm(forms.Form):
 last_name = forms.CharField(label='Фамилия', max_length=50)
 first_name = forms.CharField(label='Имя', max_length=50)
 middle_name = forms.CharField(label='Отчество', max_length=50)
 email = forms.EmailField(label='e-mail')
 birth_date = forms.DateField(label='Дата рождения')
 is_resting = forms.BooleanField(label='В отпуске', required=False, initial=True)
 speciality = forms.CharField(label='Специальность', max_length=50)
 slug = forms.SlugField(label='URL', max_length=255)