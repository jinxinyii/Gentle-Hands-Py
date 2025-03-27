from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
def medication_view(request):
    return render(request, 'medication.html')

@login_required
def illness_list(request):
    return render(request, 'illness_list.html')

@login_required
def appointment_list(request):
    return render(request, 'appointment_list.html')

@login_required
def immunization_list(request):
    return render(request, 'immunization.html')

@login_required
def medic(request):
    return render(request, 'medic.html')

@login_required
def growth_data(request):
    return render(request, 'growth_data.html')