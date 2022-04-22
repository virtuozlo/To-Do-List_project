from django.urls import path
from app_todo.views import todo_list, todo_list_create, todo_list_delete, todo_detail_update

app_name = 'app_todo'
urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_list_create, name='todo_create'),
    path('delete/', todo_list_delete, name='todo_delete'),
    path('update/<int:id>/', todo_detail_update, name='todo_update')
]
