from django.shortcuts import redirect, render
from django.http import HttpResponse

from busness_e_commerce_app.forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'index.html')

def index(request):
    return render(request, 'home.html')

def other(request):
    return render(request, 'next.html')