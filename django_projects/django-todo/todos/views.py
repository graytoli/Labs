from django.shortcuts import render, redirect

from .models import TodoItem
from .forms import TodoItemForm

def todos(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todos:todos')
    else:
        form = TodoItemForm()
    
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {'items': items, 'form': form})


