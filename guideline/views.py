from django.shortcuts import render

def guideline(request):
    return render(request, 'guideline/guideline.html')
