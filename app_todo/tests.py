from django.test import TestCase
from django.urls import reverse
import datetime
from app_todo.models import ToDo


class TestToDo(TestCase):
    """
    Тестирование приложения задач
    """

    @classmethod
    def setUpTestData(cls):
        """
        Создание задач
        :return:
        """
        for i in range(10):
            ToDo.objects.create(name=f'Задача номер {i}')

    def test_list_view_todo(self):
        """
        Тест применения шаблона, вывода объектов и его количества.
        :return:
        """
        response_list = self.client.get(reverse('todo_app:todo_list'))
        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(len(response_list.context['todo_list']), 10)
        self.assertTemplateUsed(response_list, 'app_todo/todo_list.html')

    def test_create_todo(self):
        """
        Тестирование формы создания задач
        :return:
        """
        response_todo = self.client.post(reverse('todo_app:todo_create'), {'name': 'name'})
        self.assertContains(response_todo, 'Успешно')

    def test_filter_todo(self):
        """
        Тестирование: По дате, по выполнению, показать выполненные/невыполненные задачи
        :return:
        """
        response_todo_date = self.client.post(reverse('todo_app:todo_list'), {'date': datetime.date.today()})
        self.assertEqual(response_todo_date.status_code, 200)
        response_todo_check = self.client.post(reverse('todo_app:todo_list'), {'check': False})
        self.assertEqual(response_todo_check.status_code, 200)
        response_todo_order = self.client.post(reverse('todo_app:todo_list'), {'order': 'date'})
        self.assertEqual(response_todo_order.status_code, 200)

    def test_delete_todo(self):
        """
        Тестирование удаления объекта с кверисета
        :return:
        """
        todo_len_start = ToDo.objects.all().count()
        response_del_todo = self.client.post(reverse('todo_app:todo_delete'), {'todo_id': 3})
        todo_len = ToDo.objects.all().count()
        self.assertEqual(response_del_todo.status_code, 200)
        self.assertNotEqual(todo_len, todo_len_start)

    def test_update_todo(self):
        todo_start = ToDo.objects.get(id=2)
        response_todo_update = self.client.post(reverse('todo_app:todo_update', kwargs={'id': 2}), {'name': 'names'})
        todo_start.save()
        todo_end = ToDo.objects.get(id=2).name
        self.assertEqual(response_todo_update.status_code, 200)
        self.assertNotEqual(todo_start, todo_end)
