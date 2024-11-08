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
    
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

@csrf_exempt
def upload_file(request):
    return render(request, 'upload.html')
    """
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        return JsonResponse({'file_url': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
    """