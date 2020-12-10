from django.shortcuts import render
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #Using reverse_lazy instead of reverse because it will activate only if submit button is pressed after filling up form
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
