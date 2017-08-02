from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#@login_required
def index(request):
    return HttpResponse("Hola");

def login(request):
   return render(request, auth_views.login)