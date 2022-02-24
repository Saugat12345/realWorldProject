from django.forms import ModelForm
from .models import Product, AppliedProduct


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AppliedProductForm(ModelForm):
    class Meta:
        model = AppliedProduct
        fields = '__all__'