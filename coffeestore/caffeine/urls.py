from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),  # Change the path to an empty string
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/add', views.OrderCreateView.as_view(), name='order-add'),
    path('order/<pk>/delete', views.OrderDeleteView.as_view(), name='order-del'),
    path('order/<int:pk>/edit', views.OrderEditView.as_view(), name='order-edit'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/', views.ProductListView.as_view(), name='product_list'),  
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
]
