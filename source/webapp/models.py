from django.db import models

from webapp.validate import validate_summary


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Task(BaseModel):
    summary = models.CharField(max_length=30, null=False, blank=False, verbose_name='Заголовок',
                               validators=[validate_summary])
    description = models.TextField(max_length=100, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks',
                               verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Тип')

    def __str__(self):
        return f"{self.id}. {self.summary}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Status(BaseModel):
    task_status = models.CharField(max_length=30, null=False, blank=False, verbose_name='Статус задачи')

    def __str__(self):
        return f"{self.task_status}"

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(BaseModel):
    task_type = models.CharField(max_length=30, null=False, blank=False, verbose_name='Тип задачи')

    def __str__(self):
        return f"{self.task_type}"

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
