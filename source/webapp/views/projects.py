from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class UpdateProjectUser(PermissionRequiredMixin, UpdateView):
    form_class = UserForm
    template_name = 'projects/user_update.html'
    model = Project
    permission_required = ('webapp.add_user_project', 'webapp.remove_user_project')

    def has_permission(self):
        return super().has_permission() and self.get_object().user.filter(username=self.request.user)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class CreateProject(PermissionRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'projects/create.html'
    permission_required = 'webapp.add_project'


class UpdateProject(PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = 'projects/update.html'
    model = Project
    permission_required = 'webapp.change_project'


class DeleteProject(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('webapp:projects_index')
    permission_required = 'webapp.delete_project'
