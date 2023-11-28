from django.urls import path

from web_shop_app import views

from web_shop_app.views import (
    CancelView,
    SuccessView,
    CreateCheckoutSessionView,
    ProductLandingPageView,
)

urlpatterns = [
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<int:id>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
