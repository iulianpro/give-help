from django.shortcuts import redirect, reverse
from django.contrib import auth
from home.views import index

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
