from django.urls import path
from webapp.views import IndexView, TaskView, UpdateTask, DeleteTask, ProjectsView, DetailProjectView, \
    CreateProject, CreateTaskView, UpdateProject, DeleteProject, UpdateProjectUser, CreateTask

app_name = 'webapp'

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects_index'),
    path('tasks/', IndexView.as_view(), name='index'),
    path('projects/add/', CreateProject.as_view(), name='create_project'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('project/<int:pk>/', DetailProjectView.as_view(), name='project_view'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('project/<int:pk>/update/', UpdateProject.as_view(), name='update_project'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('project/<int:pk>/delete/', DeleteProject.as_view(), name='delete_project'),
    path('project/<int:pk>/task/add/', CreateTaskView.as_view(), name='project_task_create'),
    path('project/<int:pk>/update_project_user/', UpdateProjectUser.as_view(), name='update_project_user'),
    path('tasks/add/', CreateTask.as_view(), name='create_task'),
]
