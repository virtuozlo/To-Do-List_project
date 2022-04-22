import datetime
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from django.db import models


class ToDo(models.Model):
    """
    Модель задачи
    """
    name = models.TextField(verbose_name=_('Что нужно сделать'))
    date = models.DateField(verbose_name=_('Когда выполнить'), default=now)
    check = models.BooleanField(verbose_name=_('Статус задачи'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')
