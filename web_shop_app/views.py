import stripe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from stripe.api_resources import price

from config import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return HttpResponse("Hello World!")


def detail(request, id):
    i_list = Item.objects.filter(id=id)
    context = {"id": id, "item_list": i_list}
    return render(request, "web_shop_app/item_preview.html", context)


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
                    'item': item.name,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="Test Item")
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "item": price
        })
        return context
