from django.urls import path, include
from . import views

app_name = 'markets'

urlpatterns = [
    path('location', views.location, name="location"),  
    path('product', views.product, name="product"),
    
    path('location/add', views.location_create, name="location_add"),  
    path('product/add', views.product_create, name="product_add"),
    
    path('location/<int:pk>/edit', views.location_update, name="location_update"),  
    path('product/<int:pk>/edit', views.product_update, name="product_update"),

    path('location/<int:pk>/delete', views.location_delete, name="location_delete"),  
    path('product/<int:pk>/delete', views.product_delete, name="product_delete"),

   ]