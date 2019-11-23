from django.urls import path            #To import the url function
from . import views                     # . is used to import all the views file from the project


urlpatterns = [
    path('', views.guideline),
]
