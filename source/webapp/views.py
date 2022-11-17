from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('-updated_at')
        context = {'tasks': tasks}
        return super().render_to_response(context)


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        kwargs['task'] = task
        return super().get_context_data(**kwargs)
