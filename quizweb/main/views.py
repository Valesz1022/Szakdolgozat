from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')
