from django.urls import path
from webapp.views import IndexView, TaskView, UpdateTask, CreateTask, DeleteTask, ProjectsView, DetailProjectView, \
    CreateProject, CreateTaskView, UpdateProject, DeleteProject

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects_index'),
    path('tasks/', IndexView.as_view(), name='index'),
    path('tasks/add/', CreateTask.as_view(), name='create_task'),
    path('projects/add/', CreateProject.as_view(), name='create_project'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', UpdateProject.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProject.as_view(), name='delete_project'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('project/<int:pk>/task/add/', CreateTaskView.as_view(), name='project_task_create')
]
