from django.urls import path
from . import views
from .views import HomeView, create_task, update_task, deleteTask, todo_list, todo_list_with_tasks, label_popup


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('testing', views.testing, name='testing'),
    path('calendar', views.calendar, name='calendar'),
    path('board', views.board, name='board'),
    path('list/', create_task, name='list'),
    path('update_task/<str:pk>/', update_task, name="update_task"),
    path('list/', todo_list, name='todo_list'),
    path('delete/<str:pk>/', deleteTask, name="delete"),
    path('', todo_list_with_tasks, name = "tasklist"),
    path('label/popup/', label_popup, name='label_popup'),
]

