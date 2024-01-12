from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adminDashboard", views.admin, name="adminDashboard"),
    path("clientdashord", views.clientdashord, name="clientdashord"),
    path('login/', views.login_view, name='login'),
    path("REGISTER/", views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]