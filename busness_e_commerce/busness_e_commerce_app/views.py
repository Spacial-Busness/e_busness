from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

from busness_e_commerce_app.models import Account
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html',)

def admin(request):
    if request.user.is_authenticated and request.user.account.user_role == 1:
        return render(request, 'admindashboard.html')
    else:
        messages.error(request, 'You are unauthorized to access the admin dashboard.')
        return redirect('index')

def clientdashord(request):
    return render(request, 'clientdashord.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            account = Account.objects.create(
                user=user,
                address_id=form.cleaned_data['address_id'],
                phone_number=form.cleaned_data['phone_number'],
                company_name=form.cleaned_data['company_name'],
                user_role=form.cleaned_data['user_role'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender'],
                profile_image=form.cleaned_data['profile_image'],
            )
            login(request, user)
            
            if account.user_role == 1:
                messages.success(request, 'Registration successful as role 1. You are now logged in.')
                return redirect('adminDashboard')
            elif account.user_role == 2:
                messages.success(request, 'Registration successful as role 2. You are now logged in.')
                return redirect('clientdashord')
            else:
                messages.error(request, 'Invalid user_role.')

        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.account.user_role == 1:
                messages.success(request, 'Login successful as role 1.')
                return redirect('adminDashboard')
            elif user.account.user_role == 2:
                messages.success(request, 'Login successful as role 2.')
                return redirect('clientdashord')
            else:
                messages.error(request, 'Invalid role.')

        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')