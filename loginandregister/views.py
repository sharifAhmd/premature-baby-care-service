from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def loginandregister(request):
    return render(request, 'loginandregister/loginandregister.html')



def login_user(request):

    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('profile/')
    return render_to_response('loginandregister.html', context_instance=RequestContext(request))

@login_required(login_url='/profile/')
def profile(request):
    return render(request, 'loginandregister/profile.html')
