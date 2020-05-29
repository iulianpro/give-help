from django.shortcuts import render, redirect, reverse
from subscribe.forms import EmailSignupForm


def view_cart(request):
    subscribe_form = EmailSignupForm()
    return render(request, "cart.html", {'subscribe_form': subscribe_form})


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('gifts'))


def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = int(cart[id]) + quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
