from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("busness_e_commerce_app.urls")),
    path('admin/', admin.site.urls),
]
