from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# view functions take a request and return a response. 
# in some frameworks this is known as a request handler

def say_hello(request):
    # this would be able to
        # pull data from db
        # transform data
        # send emails
    # return HttpResponse('Hello World')
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Mosh'})
    
