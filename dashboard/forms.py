from  django import forms
from .models import Customer, Employee, Order

class CustomerForm(forms.ModelForm):

    class Meta: 
        model = Customer
        fields = "__all__"

class EmployeeForm(forms.ModelForm):

    class Meta: 
        model = Employee
        fields = "__all__"


class OrderForm(forms.ModelForm):

    class Meta: 
        model = Order
        fields = "__all__"