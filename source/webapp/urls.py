from django.urls import path
from webapp.views import IndexView, TaskView, UpdateTask

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='update_task')
]
