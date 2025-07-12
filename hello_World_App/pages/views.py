from django.shortcuts import render
from django.http import HttpResponse

def fn(request):
    return HttpResponse("hello world");
