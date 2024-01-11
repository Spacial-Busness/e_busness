from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

from busness_e_commerce_app.models import Account
from .forms import RegistrationForm

def index(request):
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

            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def other(request):
    users = Account.objects.all()
    return render(request, 'next.html', {'users': users})


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

            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')
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
            messages.success(request, 'Login successful.')
            return redirect('index')  # Redirect to the desired page after login
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')