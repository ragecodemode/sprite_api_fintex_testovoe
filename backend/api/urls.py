from django.urls import path
from .views import (
    BuyItemView,
    BuyOrderView,
    GetItemView,
    GetOrderView,
    SuccessView,
    CancelView
)

app_name = 'api'

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('item/<int:pk>/', GetItemView.as_view(), name='item'),
    path('order/<int:pk>/', GetOrderView.as_view(), name='order'),
    path(
        'buy/<int:pk>/',
        BuyItemView.as_view(),
        name='create-checkout-session'
    ),
    path(
        'order_buy/<int:pk>/',
        BuyOrderView.as_view(),
        name='create-checkout-session-order'
    ),
]
