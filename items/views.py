import stripe
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
# from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Price, Item, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


class ItemListView(View):
    """Представление для отображения всех товаров"""

    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        context = {
            'items': items,
        }
        return render(request, 'items/item_list.html', context)


class ItemDetailView(TemplateView):
    """Представление для отображения одного товара"""

    template_name = 'items/item.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        prices = Price.objects.filter(item=item)
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'prices': prices
        })
        return context


class CreateCheckoutSessionView(View):
    """Представление для создания сессии оплаты одного товара"""

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        selected_currency = request.POST.get('currency')
        price = Price.objects.get(item=item, currency=selected_currency)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    """Представление для отображения успешного завершения оплаты"""

    template_name = "status/success.html"


class CancelView(TemplateView):
    """Представление для отображения отмененной оплаты"""

    template_name = "status/cancel.html"


class OrderView(View):
    """Представление для отображения корзины товаров"""

    template_name = 'order/order.html'

    def get(self, request, *args, **kwargs):
        session_id = request.session.session_key
        currencies = Price.objects.values_list(
            'currency', flat=True
        ).distinct()

        order_items = OrderItem.objects.filter(
            session_id=session_id
        ).prefetch_related('item').all()

        context = ({
            'order_items': order_items,
            'currencies': currencies
        })

        return render(request, self.template_name, context)


class AddToOrderView(View):
    """Представление для добавления товара в корзину заказа."""

    def post(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(Item, id=item_id)
        session_id = request.session.session_key
        quantity = int(request.POST.get('quantity', 1))

        # Ищем OrderItem для данного товара и заказа
        order_item = (
            OrderItem.objects.filter(session_id=session_id, item=item).first()
        )

        # Если OrderItem не существует, создаем новый
        if not order_item:
            order_item = (
                OrderItem.objects
                .create(session_id=session_id, item=item, quantity=quantity)
            )
        else:
            # Иначе обновляем количество товара в заказе
            order_item.quantity += quantity
            order_item.save()

        return redirect('item-list')


class RemoveFromOrderView(View):
    """Представление для удаления товара из корзины заказа."""

    def get(self, request, order_item_id, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=order_item_id)
        order_item.delete()
        return redirect('order')


class CreateCheckoutSessionOrderView(View):
    """Представление для создания сессии оплаты корзины заказа."""

    def post(self, request, *args, **kwargs):
        # Получаем товары из корзины
        session_id = request.session.session_key
        order_items = OrderItem.objects.filter(session_id=session_id)

        selected_currency = request.POST.get('currency')

        # Создаем список товаров для сессии оплаты
        line_items = []

        # Добавляем товары из корзины в список
        for order_item in order_items:
            price = (
                Price.objects
                .get(item=order_item.item, currency=selected_currency)
            )
            line_items.append({
                'price': price.stripe_price_id,
                'quantity': order_item.quantity,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
            currency=selected_currency,
        )
        return redirect(checkout_session.url)
