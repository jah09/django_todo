from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
 
    path('create-todo/',  views.create_todo, name='create-todo'),
    path('delete-todo/<str:pk>/',  views.delete_todos, name='delete-todo'),
    path('edit-todo/<str:pk>/',  views.edit_todo, name='edit-todo')

]
