from django import forms
from app_todo.models import ToDo
import logging

logger = logging.getLogger(__name__)


class ToDoForms(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ['name', 'check']
