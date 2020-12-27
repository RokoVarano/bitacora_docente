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
    success_url = '/login/'

    def get_name(self, request):
    # if this is a POST request we need to process the form data
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            # redirect to a new URL:
            return HttpResponseRedirect('login/')

    # if a GET (or any other method) we'll create a blank form
      else:
        form = LoginForm()

      return render(request, '', {'form': form})