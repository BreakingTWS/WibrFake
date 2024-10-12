from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('generate_204/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
