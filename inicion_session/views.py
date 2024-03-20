from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.template import RequestContext


from django.views.decorators.csrf import csrf_protect



@csrf_protect
@login_required
def home_view(request):
    return render(request, 'home.html',context_instance=RequestContext(request))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login',context_instance=RequestContext(request))

@login_required
def profile_view(request):
    return render(request, 'profile.html',context_instance=RequestContext(request))
