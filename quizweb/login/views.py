from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Ha a form érvényes, próbálj bejelentkezni a felhasználóval
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Átirányítás a főoldalra
            else:
                form.add_error(None, "Invalid username or password")  # Hibaüzenet hozzáadása a form-hoz
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')