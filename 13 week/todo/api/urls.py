from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.Tasklist.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('login/', views.logout),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    #path('task_lists/<int:pk>/tasks', views.ListTask.as_view()),
]
