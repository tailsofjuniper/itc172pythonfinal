from .models import Todo, Details
from django.shortcuts import render, get_object_or_404

def index (request):
    return render(request, 'finalapp/index.html')
# Create your views here.

def gettodo (request):
    todo_list=Todo.objects.all()
    return render(request, 'finalapp/todo.html' ,{'todo_list' : todo_list})
def getdetails (request, id):
    todo_detail=get_object_or_404(Details, pk=id)
    todo_location=todo_detail.todolocation

    # agenda=todo.objects.filter(todoagenda=id).count()
    context={
        'todo_detail' : todo_detail,
        'todo_location' : todo_location,
    }
    return render(request, 'finalapp/details.html', context=context)