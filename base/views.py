from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def home(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Todo.objects.create(title=title, description=description)

    context = {'todos': todos}
    return render(request, 'base/home.html', context)


def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Todo.objects.create(title=title, description=description)

        return redirect('home')

    # context = {}
    return render(request, 'base/todo_form.html')


def todos(request):

    todos = Todo.objects.all()
    print(todos)
    context = {
        'todos': todos
    }
    return render(request, 'base/home.html', context)


def delete_todos(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')


def edit_todo(request, pk):
    page='edit'
    todo = Todo.objects.get(id=pk)
    print("title", todo.title)
    if request.method == 'POST':

        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('home')

    context = {'todo': todo, 'page': page}

  
    return render(request, 'base/todo_form.html',context)


    
  
  