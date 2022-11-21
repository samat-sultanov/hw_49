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


class UpdateTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm(initial={
                'summary': self.task.summary,
                'description': self.task.description,
                'status': self.task.status,
                'type': self.task.type.all()
            })
            return render(request, 'update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.summary = form.cleaned_data.get('summary')
            self.task.description = form.cleaned_data.get('description')
            self.task.status = form.cleaned_data.get('status')
            self.task.type.set(form.cleaned_data.pop('type'))
            self.task.save()
            return redirect('task_view', pk=self.task.pk)
        return render(request, 'update.html', {'form': form})


class CreateTask(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, 'create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.pop('type')
            new_task = Task.objects.create(summary=summary, description=description,
                                           status=status)
            new_task.type.set(type)
            return redirect('task_view', pk=new_task.pk)
        return render(request, 'create.html', {'form': form})


class DeleteTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, 'delete.html', {'task': self.task})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.task.delete()
            return redirect('index')