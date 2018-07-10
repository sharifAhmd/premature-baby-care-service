from django.shortcuts import render
from problemandsolution.models import problemandsolution

def get(request):
    items = problemandsolution.objects.all()
    args = {
        'items': items
    }
    return render(request, 'problemandsolution/problemandsolution.html', args)



