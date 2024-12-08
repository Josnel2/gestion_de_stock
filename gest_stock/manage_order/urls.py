from django.urls import path
from .views import ProductListCreateView, ProductDetailView,ProviderListCreateView, ProviderDetailView,OrderDetailView,OrderListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),  
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  
    path("providers/", ProviderListCreateView.as_view(), name="provider_create"),
    path("providers/<int:pk>/", ProviderDetailView.as_view(), name="provider_detail"),
    path("Order/", OrderListCreateView.as_view(), name="Order_create"),
    path("Order/<int:pk>/", OrderListCreateView.as_view(), name="Order_detail"),
    
]
