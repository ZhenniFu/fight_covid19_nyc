from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'map.html')


def dashboard(request):
  return render(request, 'dashboard.html')


def table(request):
  return render(request, 'table.html')
