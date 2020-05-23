from django.shortcuts import render
from .models import Gift


def all_gifts(request):
    gifts = Gift.objects.all()
    return render(request, 'gifts.html', {'gifts': gifts})
