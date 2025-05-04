from django.urls import path
from .views import ProductListCreateView, ProductDetailView,ProviderListCreateView, ProviderDetailView,OrderDetailView,OrderListCreateView,StatistiquesAPIView, ProduitsLesPlusVendusAPIView,UpdateStockView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'), 
    path('stock/', UpdateStockView.as_view(), name='stock_v'),  
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  
    path("providers/", ProviderListCreateView.as_view(), name="provider_create"),
    path("providers/<int:pk>/", ProviderDetailView.as_view(), name="provider_detail"),
    path("Order/", OrderListCreateView.as_view(), name="Order_create"),
    path("Order/<int:pk>/", OrderDetailView.as_view(), name="Order_detail"),
    path('statistiques/', StatistiquesAPIView.as_view(), name='statistiques'),
    path('produits-les-plus-vendus/', ProduitsLesPlusVendusAPIView.as_view(), name='produits_les_plus_vendus'),
]


