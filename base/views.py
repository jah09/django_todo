from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Todo.objects.create(title=title, description=description)
 

    context = {   'todos': todos}
    return render(request, 'base/index.html', context)


# def create_todo(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         print(title, description)
#         Todo.objects.create(title=title, description=description)
#         return redirect('index.html')
#
#
#     context = {}
#     return render(request, 'base/index.html', context)


def todos(request):

    todos = Todo.objects.all()

    context = {
        'todos': todos
    }
    return render(request, 'base/index.html', context)


def delete_todos(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect(request, 'base/index.html')
