from django.http import HttpResponse
from django.shortcuts import render, redirect
import stripe

from config import settings
from .models import Item

from flask import Flask, redirect

app = Flask(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return HttpResponse("Hello World!")


def detail(request, id):
    i_list = Item.objects.filter(id=id)
    context = {"id": id, "item_list": i_list}
    return render(request, "web_shop_app/item_preview.html", context)


@app.route('/item', methods=['POST'])
def item():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:8000/success',
    cancel_url='http://localhost:8000/cancel',
  )

  return redirect(session.url, code=303)
