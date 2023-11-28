from django.urls import path

from web_shop_app import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("item/<int:id>/", views.detail, name="detail"),
    path("item/", views.item, name="item"),
]
