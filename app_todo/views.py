import datetime
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from app_todo.models import ToDo
from app_todo.forms import ToDoForms


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
    if request.method == 'GET':
        todo_list = ToDo.objects.filter(date=datetime.date.today())
        return render(request, 'todo_app/todo_list.html', {'todo_list': todo_list})
    elif request.method == 'POST':
        if 'date' in request.POST:  # Вывод задач на дату
            date = request.POST.get('date')
            if not date:  # Если поле пустое
                date = datetime.date.today()
            todo_list = ToDo.objects.filter(date=date)

        elif 'order' in request.POST:
            how_sort = request.POST.get('order')  # Сортировка по дате либо выполнению
            todo_list = ToDo.objects.all().order_by(f'-{how_sort}')

        elif 'check' in request.POST:
            todo_list = ToDo.objects.filter(check=True)  # Показать выполненные задачи
        elif 'uncheck' in request.POST:
            todo_list = ToDo.objects.filter(check=False)  # Невыполненные соотвественно
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
    if request.method == 'GET':
        empty_form = ToDoForms()
        return render(request, 'todo_app/todo_create.html', {'form': empty_form})
    elif request.method == 'POST':
        form = ToDoForms(request.POST)
        if form.is_valid():
            date = request.POST.get('date')
            form.date = date
            title = _('Успешно')
            text = _('Задача создана!')
            form.save()
            return render(request, 'all_answers.html', {'title': title, 'text': text})
        else:
            title = _('Ошибка!')
            text = form.errors
            return render(request, 'all_answers.html', {'title': title, 'text': text})


def todo_list_delete(request):
    """
    Удалить задачу

    **Template:**

    :template:`templates/all_answers.html`
    """
    if request.method == 'POST':
        id_todo = int(request.POST.get('todo_id'))
        ToDo.objects.get(id=id_todo).delete()
        title = _('Успешно!')
        text = _('Задача удалена')
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
    if request.method == 'GET':
        todo = ToDo.objects.only('name', 'date').get(id=id)
        form = ToDoForms(initial={'name': todo.name})
        return render(request, 'todo_app/todo_update.html', {'todo': todo,
                                                             'form': form})
    elif request.method == 'POST':
        form_todo = ToDoForms(request.POST)
        if form_todo.is_valid():
            form_todo.save()
            title = _('Успешно!')
            text = _('Задача успешно изменена!')
            return render(request, 'all_answers.html', {'title': title, 'text': text})
        else:
            title = _('Ошибка!')
            text = form_todo.errors
            return render(request, 'all_answers.html', {'title': title, 'text': text})
