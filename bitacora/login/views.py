from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import generic
from django.db import models
from login.forms import LoginForm

# Create your views here.

class LoginView (generic.FormView):
    model = User
    template_name = 'login/index.html'
    form_class = LoginForm
    success_url = 'menu'
    
    def identificar_user(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          context = {'user': user}
          return render(request, 'menu', context)
        else:
          return HttpResponse('usuario invalido')