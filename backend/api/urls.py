from django.urls import path
from .views import (
    BuyItemView,
    GetItemView,
    SuccessView,
    CancelView
)

app_name = 'api'

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('item/<int:pk>/', GetItemView.as_view(), name='item'),
    path(
        'buy/<int:pk>/',
        BuyItemView.as_view(),
        name='create-checkout-session'
    ),
]
