from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.main, name="main"),
    path('customers', views.customer, name="customers"),  
    path('employee', views.employee, name="employees"),
    path('orders', views.order, name="orders"),
    
    path('customers/add', views.customer_create, name="customers_add"),  
    path('employees/add', views.employee_create, name="employees_add"),
    path('orders/add', views.order_create, name="orders_add"),
    
    path('customers/<int:pk>/edit', views.customer_update, name="customers_update"),  
    path('employees/<int:pk>/edit', views.employee_update, name="employees_update"),
    path('orders/<int:pk>/edit', views.order_update, name="orders_update"),

    path('customers/<int:pk>/delete', views.customer_delete, name="customers_delete"),  
    path('employees/<int:pk>/delete', views.employee_delete, name="employees_delete"),
    path('orders/<int:pk>/delete', views.order_update, name="orders_delete"),

   ]