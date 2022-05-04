from rest_framework import viewsets
from app_todo.models import ToDo
from app_todo_api.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    Представления для отображения Сериализованной модели
    """
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
