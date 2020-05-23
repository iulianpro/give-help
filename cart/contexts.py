from django.shortcuts import get_object_or_404
from gifts.models import Gift


def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    gift_count = 0

    for id, quantity in cart.items():
        gift = get_object_or_404(Gift, pk=id)
        total += quantity * gift.price
        gift_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'gift': gift})

    return {'cart_items': cart_items, 'total': total, 'gift_count': gift_count}
