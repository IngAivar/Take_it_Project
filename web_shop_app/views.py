import stripe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from stripe.api_resources import price

from config import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["id"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': item.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success',
            cancel_url=domain + '/cancel',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "web_shop_app/success.html"


class CancelView(TemplateView):
    template_name = "web_shop_app/cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "web_shop_app/landing.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="Test Item")
        prices = Item.objects.filter(id=item.id)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": item,
            "prices": prices
        })
        return context
