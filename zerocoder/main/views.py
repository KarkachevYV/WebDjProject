from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<p>Это 1 страничка через HttpResponse</p>')

def new(request):
  return HttpResponse('<p>Это 2 страничка через HttpResponse</p>')

def data(request):
  return HttpResponse('<p>ПРИВЕТ через HttpResponse</p>')

def test(request):
  return HttpResponse('<p>ПОКА через HttpResponse</p>')