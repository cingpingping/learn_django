from re import X
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def calculate():
    x = 10
    y = 2
    return x

def say_hello(request):
    # this can be:
    # pull data from db 
    # transform
    # send email
    
    # return HttpResponse('Hello World')
    x = calculate()
    return render(request, 'hello.html', {'name': "Ade"})