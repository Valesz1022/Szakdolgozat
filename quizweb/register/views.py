from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    errors = []
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            errors = form.errors
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'errors': errors})

