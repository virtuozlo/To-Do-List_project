from django import forms
from app_todo.models import ToDo


class ToDoForms(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'check']
