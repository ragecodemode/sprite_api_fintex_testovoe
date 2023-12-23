import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings

from payments.models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_KEY

YOUR_DOMAIN = 'http://127.0.0.8000'


class SuccessView(TemplateView):
    """TemplateView для успешной оплаты."""
    template_name = 'success.html'


class CancelView(TemplateView):
    """TemplateView для отмены оплаты."""
    template_name = 'cancel.html'


class BuyItemView(View):
    """View для оплаты выбранного Item."""

    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': item.currency,
                            'product_data': {
                                'name': item.name,
                                'description': item.description,
                            },
                            'unit_amount': int(item.price * 100),
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as errore:
            return JsonResponse({'error': str(errore)})


class GetItemView(TemplateView):
    """TemplateView для полуения информации о выбранном Item."""

    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        item_pk = self.kwargs.get('pk')
        item = Item.objects.get(pk=item_pk)
        context = super(GetItemView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class BuyOrderView(View):
    """View для оплаты заказа Order."""

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': order.item.currency,
                            'product_data': {
                                'name': order.item.name,
                                'description': order.item.description,
                            },
                            'unit_amount': order.total_price,
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as errore:
            return JsonResponse({'error': str(errore)})


class GetOrderView(TemplateView):
    """TemplateView для полуения информации о заказе Order."""

    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        order_pk = self.kwargs.get('pk')
        order = Order.objects.get(pk=order_pk)
        context = super(GetOrderView, self).get_context_data(**kwargs)
        context.update({
            'order': order,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'order_total_price': order.total_price
        })
        return context
