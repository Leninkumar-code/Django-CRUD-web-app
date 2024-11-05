from app_crud.models import student
from django import forms

class StudentForm (forms.ModelForm):
    class Meta :
        model = student
        fields = ['name','age','place'] # '__all__'
      # excluede = 'age' -|------------It excludes the mentioned field.