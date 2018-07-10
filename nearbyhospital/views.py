from django.shortcuts import render

def nearbyhospital(request):
    return render(request, 'nearbyhospital/nearbyhospital.html')
