from django.shortcuts import render, redirect, reverse


def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))
