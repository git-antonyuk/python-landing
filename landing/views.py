# from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
  title = 'Hello World'
  description = '42 42 42'
  return render(request, './index.html', {
    'title': title,
    'description': description
  })