from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('hello', views.say_hello),
    path('upload/', views.upload_file, name='upload_file'), 
]
