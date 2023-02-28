from django import forms
from .models import Location, Product

class LocationForm(forms.ModelForm):

    class Meta: 
        model = Location
        fields = "__all__"


class ProductForm(forms.ModelForm):

    class Meta: 
        model = Product
        fields = "__all__"

