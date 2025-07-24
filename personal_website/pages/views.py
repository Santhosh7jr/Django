from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint

# Create your views here.

def fn(request):
    return HttpResponse("homePage")

def about_page(request):

    context={
        "name":"santhosh",
        "age":20
    }

    return render(request,"pages/about.html",context)
