from django.urls import path
from .views import TaskListView, CreatTaskView, DetailTaskView, DeleteTaskView, UpdateTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('task/new/', CreatTaskView.as_view(), name='task_new'),
    path('task/<int:pk>', DetailTaskView.as_view(), name='task_detail'),
    path('task/<int:pk>/delete', DeleteTaskView.as_view(), name='delete-task'),
    path('task/<int:pk>/edit', UpdateTaskView.as_view(), name='update-task'),

]