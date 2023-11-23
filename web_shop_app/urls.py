from django.urls import path

from web_shop_app import views

urlpatterns = [
    path("", views.index, name="index"),

]
