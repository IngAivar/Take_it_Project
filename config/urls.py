from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('web_shop_app/', include("web_shop_app.urls")),
    path('', include("web_shop_app.urls")),
    path('admin/', admin.site.urls),
]
