from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Usuario
from django.urls import reverse

def index(request):
	return render(request, 'index.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		return HttpResponse('Hola')
		#user = authenticate(request, username=username, password=password)
		#if user is not None:
			#login(request, user)
			#return redirect('home')
		#else:
			#return render(request, 'login.html')
			#return HttpResponse(request.method)
			#aa = Usuario.objects.get(username=username)
			#return HttpResponse(username==username)

def logout(request):
    return redirect('login')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')
    
def mostrar_credenciales(request):
    credenciales = Usuario.objects.all()
    for credencial in credenciales:
        print(f"Usuario: {credencial.username}")
        print(f"Contraseña: {credencial.password}")
        print(f"Grupos: {credencial.groups.all()}")
        print(f"Permisos: {credencial.user_permissions.all()}")
    return HttpResponse("Credenciales mostradas en la terminal")
