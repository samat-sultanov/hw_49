from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import ProjectForm
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


class CreateProject(CreateView):
    form_class = ProjectForm
    template_name = 'projects/create.html'


class UpdateProject(UpdateView):
    form_class = ProjectForm
    template_name = 'projects/update.html'
    model = Project