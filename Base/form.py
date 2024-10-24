from django import forms
from .models import RegisterUpload

class StudentForms(forms.ModelForm):
  class Meta:
    model = RegisterUpload
    fields = '__all__'

    widgets = {
      'first_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
       'last_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
        'dob' : forms.DateInput(attrs={
        'class' : 'form-control',
        'type' : 'Date'
      }),
      'school' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'grade' : forms.NumberInput(attrs={
        'class' : 'form-control'
      }),
      'email' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'address' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'id_number' : forms.NumberInput(attrs={
        'class' : 'form-control'
      }),
    }