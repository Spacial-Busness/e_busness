from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/", views.other, name="product"),
    path('login/', views.login_view, name='login'),
    path("REGISTER/", views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]