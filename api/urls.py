from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('user/', include('api.user.urls')),
]


