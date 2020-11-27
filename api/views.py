from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from django.views.generic import DetailView
# class MyView(ListView):
#     template_name = 'api/index.html'
from django.http import HttpResponse
from django.contrib.auth.models import User
class Detail(DetailView):
    template_name = 'api/index.html'
    model = User
class List(ListView):
    model=User