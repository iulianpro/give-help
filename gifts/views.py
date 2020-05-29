from django.shortcuts import render
from .models import Gift
from subscribe.forms import EmailSignupForm


def all_gifts(request):
    gifts = Gift.objects.all()
    subscribe_form = EmailSignupForm()
    return render(request, 'gifts.html', {'gifts': gifts, 'subscribe_form': subscribe_form})
