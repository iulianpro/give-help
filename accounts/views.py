from django.shortcuts import redirect, reverse, render
from django.contrib import auth, messages
from home.views import index

# Create your views here.


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse('index'))


def login(request):
    return render(request, 'login.html')
