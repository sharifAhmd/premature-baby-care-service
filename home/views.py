from django.shortcuts import render,HttpResponse        #render is a shorcut function for managing the http request or response

def home(request):
    return render(request, 'home/home.html')
