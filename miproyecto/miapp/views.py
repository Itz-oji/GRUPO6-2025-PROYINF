from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse


def index(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'index.html', {'profile': profile})
    
def inicio(request):
    return render(request, 'index.html')

def login_view(request):
    return HttpResponse("¡Sesión iniciada con Google correctamente!")
