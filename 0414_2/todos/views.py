from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from todos.forms import TodoForm
from .models import Todo
# Create your views here.
@require_safe
def index(request):

    if request.user.is_authenticated:

        todos = Todo.objects.order_by('-pk')
        context = {
            'todos': todos,
        }
        return render(request, 'todos/index.html', context)
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
def new(request):
    if request.user.is_authenticated:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return render(request, 'todos.create.html')
    return redirect('accounts:login')