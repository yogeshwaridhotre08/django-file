# tasks/urls.py
from django.urls import path
from .views import user_logout,task_list, task_detail, task_create, task_edit, task_delete,register,user_login

urlpatterns = [
    path('task_list', task_list, name='task_list'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('new/', task_create, name='task_create'),
    path('<int:pk>/edit/', task_edit, name='task_edit'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
     path('', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
