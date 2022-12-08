from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View

from django.views.generic import TemplateView, ListView, UpdateView

from webapp.forms import TaskForm, SearchForm
from webapp.models import Task


class IndexView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['-updated_at']
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Task.objects.filter(
                Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context['query'] = query
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class TaskView(TemplateView):
    template_name = 'tasks/task_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class UpdateTask(UpdateView):
    form_class = TaskForm
    template_name = 'tasks/update.html'
    model = Task

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class CreateTask(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = TaskForm()
            return render(request, 'tasks/create.html', {'form': form})

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
        return render(request, 'tasks/create.html', {'form': form})


class DeleteTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, 'tasks/delete.html', {'task': self.task})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.task.delete()
            return redirect('projects_index')
