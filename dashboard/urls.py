from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.main, name="main"),
    path('customers', views.customer, name="customer"),  
    path('employees', views.employee, name="employee"),
    path('orders', views.order, name="order"),
    
    path('customers/add', views.customer_create, name="customer_add"),  
    path('employees/add', views.employee_create, name="employee_add"),
    path('orders/add', views.order_create, name="order_add"),
    
    path('customers/<int:pk>/edit', views.customer_update, name="customer_update"),  
    path('employees/<int:pk>/edit', views.employee_update, name="employee_update"),
    path('orders/<int:pk>/edit', views.order_update, name="order_update"),

    path('customers/<int:pk>/delete', views.customer_delete, name="customer_delete"),  
    path('employees/<int:pk>/delete', views.employee_delete, name="employee_delete"),
    path('orders/<int:pk>/delete', views.order_update, name="order_delete"),

    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),

   ]