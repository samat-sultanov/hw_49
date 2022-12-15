from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import TaskForm
from webapp.models import Project


class CreateTaskView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})
