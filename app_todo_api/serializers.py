from rest_framework import serializers
from app_todo.models import ToDo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Сериализатор модели задач для создания API
    """
    class Meta:
        model = ToDo
        fields = '__all__'
