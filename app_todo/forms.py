from django import forms
from app_todo.models import ToDo
from django.utils.translation import gettext_lazy as _


class ToDoForms(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name','check']


class DateForm(forms.Form):
    date = forms.DateField(help_text=_('Ведите дату для сортировки мм/дд/гггг'))
