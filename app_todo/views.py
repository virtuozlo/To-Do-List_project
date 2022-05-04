import datetime

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from app_todo.models import ToDo
from app_todo.forms import ToDoForms
import logging

if settings.DEBUG:
    logger = logging.getLogger('django')
else:
    logger = logging.getLogger(__name__)


def todo_list(request):
    """
    Список всех дел. Сперва выводятся задачи на текущий день

    **Context**

    ``todo``
    An instance of :model:`app_todo.Todo`.

    **Template**
        :template:`templates/app_todo/todo_list.html`
    """
    global todo_list
    logger.info(f'{request.user}')
    if request.method == 'GET':
        logger.info(f'{request.user} method-GET ')
        todo_list = ToDo.objects.filter(date=datetime.date.today())
        return render(request, 'todo_app/todo_list.html', {'todo_list': todo_list})
    elif request.method == 'POST':
        logger.info(f'{request.user} method POST ')
        if 'date' in request.POST:  # Вывод задач на дату
            logger.info(f'{request.user} POST "date"')
            date = request.POST.get('date')
            if not date:  # Если поле пустое
                date = datetime.date.today()
            todo_list = ToDo.objects.filter(date=date)
        elif 'order' in request.POST:
            logger.info(f'{request.user} POST "order"')
            how_sort = request.POST.get('order')  # Сортировка по дате либо выполнению
            todo_list = ToDo.objects.all().order_by(f'-{how_sort}')
        elif 'check' in request.POST:
            logger.info(f'{request.user} POST "check"')
            todo_list = ToDo.objects.filter(check=True)  # Показать выполненные задачи
        elif 'uncheck' in request.POST:
            logger.info(f'{request.user} POST "uncheck"')
            todo_list = ToDo.objects.filter(check=False)  # Невыполненные соотвественно
        logger.info(f'{request.user} end POST')
        return render(request, 'todo_app/todo_list.html', {'todo_list': todo_list})


def todo_list_create(request):
    """
    Добавить задачу

    **Context**

    ``todo``
        An instance of :model:`app_todo.Todo`.

    ``empty_form / form``
        Форма

    ``date``
        Дата из шаблона

    **Template:**

    :template:`templates/app_todo/create.html`
    """
    logger.info(f'{request.user} ')
    if request.method == 'GET':
        logger.info(f'{request.user} GET(formcreate)')
        empty_form = ToDoForms()
        return render(request, 'todo_app/todo_create.html', {'form': empty_form})
    elif request.method == 'POST':
        logger.info(f'{request.user} POST ')
        form = ToDoForms(request.POST)
        if form.is_valid():
            logger.info(f'{request.user} form_is_valid')
            date = request.POST.get('date')
            form.date = date
            title = _('Успешно')
            text = _('Задача создана!')
            form.save()
            logger.info(f'{request.user} create todo')
            return render(request, 'all_answers.html', {'title': title, 'text': text})
        else:
            logger.error(f'form is no valid {form.errors}')
            title = _('Ошибка!')
            text = form.errors
            return render(request, 'all_answers.html', {'title': title, 'text': text})


def todo_list_delete(request):
    """
    Удалить задачу

    **Template:**

    :template:`templates/all_answers.html`
    """
    logger.info(f'{request.user} ')
    if request.method == 'POST':
        logger.info(f'{request.user} POST удалить задачу решил ')
        id_todo = int(request.POST.get('todo_id'))
        ToDo.objects.get(id=id_todo).delete()
        title = _('Успешно!')
        text = _('Задача удалена')
        logger.info(f'{request.user} delete todo')
        return render(request, 'all_answers.html', {'title': title, 'text': text})


def todo_detail_update(request, id: int):
    """
     Translators: Функция изменения и просмотра задачи

    **Context**

    ``todo``
        An instance of :model:`app_todo.Todo`.

    **Template:**

    :template:`templates/app_todo/todo_update.html`
    :param id: Идентификатор задачи
    """
    logger.info(f'{request.user} ')
    if request.method == 'GET':
        logger.info(f'{request.user} GET form')
        todo = ToDo.objects.only('name', 'date').get(id=id)
        form = ToDoForms(initial={'name': todo.name})
        return render(request, 'todo_app/todo_update.html', {'todo': todo,
                                                             'form': form})
    elif request.method == 'POST':
        logger.info(f'{request.user} POST')
        form_todo = ToDoForms(request.POST)
        if form_todo.is_valid():
            logger.info(f'{request.user} form is_valid')
            task = ToDo.objects.get(id=id)
            task.name = form_todo.cleaned_data.get('name')
            task.check = form_todo.cleaned_data.get('check')
            task.save()
            title = _('Успешно!')
            text = _('Задача успешно изменена!')
            logger.info(f'{request.user} update todo')
            return render(request, 'all_answers.html', {'title': title, 'text': text})
        else:
            logger.error(f'form no valid {form_todo.errors}')
            title = _('Ошибка!')
            text = form_todo.errors
            return render(request, 'all_answers.html', {'title': title, 'text': text})
