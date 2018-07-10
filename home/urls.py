from django.urls import path            #To import the url function
from . import views                     # . is used to import all the views file from the project

urlpatterns = [
    path('', views.home),               #Here in views.home: home is the funcition name in the views file
]

