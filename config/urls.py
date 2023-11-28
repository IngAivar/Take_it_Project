from django.contrib import admin
from django.urls import path, include

from web_shop_app.views import (
    CancelView,
    SuccessView,
    CreateCheckoutSessionView,
    ProductLandingPageView,
)

urlpatterns = [
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<int:id>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
