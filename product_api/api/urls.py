from django.urls import path
from . import views

urlpatterns =[
    path('',views.apiOverview, name='apiOverview'),
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-details/<int:pk>/', views.ViewProduct, name='products-details'),
    path('product-create/', views.CreateProduct, name='products-create'),
    path('product-update/<int:pk>/', views.UpdateProduct, name='product-Update'),
    path('product-delete/<int:pk>/', views.DeleteProduct, name='product-Delete'),
]