from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greet(request):
    # return HttpResponse("Hello")
    return render(request,'hello.html',{"name":"ABCS"}) # template rendering

def post(request,id):
    return HttpResponse(id)