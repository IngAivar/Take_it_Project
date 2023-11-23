from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


def index(request):
    return HttpResponse("Hello World!")


def detail(request, id):
    i_list = Item.objects.filter(id=id)
    context = {"id": id, "item_list": i_list}
    return render(request, "web_shop_app/item_preview.html", context)
