from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('create-todo/', views.create_todo, name='create-todo'),
    path('get-todos/',  views.todos, name='get-todos'),
    path('delete-todo/<str:pk>/',  views.delete_todos, name='delete-todo')
]
