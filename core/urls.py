from django.urls import path
from .views import IndexView, ItemDetailView, add_to_cart

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
]
