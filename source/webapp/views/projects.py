from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse

from webapp.forms import ProjectForm, UserForm
from webapp.models import Project


class ProjectsView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    ordering = ['-updated_at']


class DetailProjectView(DetailView):
    template_name = 'projects/project_view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.object
        return context


class UpdateProjectUser(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    template_name = 'projects/user_update.html'
    model = Project

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class CreateProject(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'projects/create.html'


class UpdateProject(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = 'projects/update.html'
    model = Project


class DeleteProject(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('webapp:projects_index')
