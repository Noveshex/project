from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('product/<slug>', views.ProductDetail.as_view(), name='product'),
]

