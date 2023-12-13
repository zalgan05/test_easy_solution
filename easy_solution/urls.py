from django.contrib import admin
from django.urls import path
from items.views import (
    CreateCheckoutSessionView,
    CreateCheckoutSessionOrderView,
    SuccessView,
    CancelView,
    ItemDetailView,
    ItemListView,
    OrderView,
    AddToOrderView,
    RemoveFromOrderView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', ItemListView.as_view(), name='item-list'),
    path('item/<pk>/', ItemDetailView.as_view(), name='item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path(
        'create-checkout-session/<pk>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    ),
    path(
        'create-checkout-session-order/',
        CreateCheckoutSessionOrderView.as_view(),
        name='create-checkout-session-order'
    ),
    path('order/', OrderView.as_view(), name='order'),
    path(
        'add-to-order/<item_id>/',
        AddToOrderView.as_view(),
        name='add-to-order'
    ),
    path(
        'remove-from-order/<order_item_id>/',
        RemoveFromOrderView.as_view(),
        name='remove-from-order'
    ),
]
