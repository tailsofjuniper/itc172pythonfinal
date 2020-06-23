from .models import Todo, Details
from .forms import TodoForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'finalapp/index.html')
# Create your views here.

def todo (request):
    todo_list=Todo.objects.all()
    return render(request, 'finalapp/todo.html' ,{'todo_list' : todo_list})

def details (request, id):
    todo_detail=get_object_or_404(Details, pk=id)
    todo_location=todo_detail.todolocation

    # agenda=todo.objects.filter(todoagenda=id).count()
    context={
        'todo_detail' : todo_detail,
        'todo_location' : todo_location,
    }
    return render(request, 'finalapp/details.html', context=context)

def loginmessage(request):
    return render(request, 'finalapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'finalapp/logoutmessage.html')

    # @login_required
def newTodo(request):
     form=TodoForm
     if request.method=='POST':
          form=TodoForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=TodoForm()
     else:
          form=TodoForm()
     return render(request, 'finalapp/newproduct.html', {'form': form})