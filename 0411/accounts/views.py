from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):

    if request.method == 'Post':
        AuthenticationForm(request, request.Post)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('articles:index')