from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'main/index.html', {'caption':"Фреймворка Django"})

def new(request):
 return render(request, 'main/new.html',  {'caption':"Фреймворка Django"})

def data(request):
   return render(request, 'main/data.html',  {'caption':"Фреймворк Django"})
def test(request):
   return render(request, 'main/test.html',  {'caption':"Фреймворка Django"})