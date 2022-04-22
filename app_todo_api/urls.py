from django.urls import path, include
from app_todo.models import ToDo
from rest_framework import routers, serializers, viewsets
from app_todo_api.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
