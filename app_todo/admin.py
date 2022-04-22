from django.contrib import admin
from app_todo.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass
