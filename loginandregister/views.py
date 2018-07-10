from django.shortcuts import render

def loginandregister(request):
    return render(request, 'loginandregister/loginandregister.html')
