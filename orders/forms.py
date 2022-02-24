from django.forms import ModelForm
from .models import Order2


class OrderForm(ModelForm):
    class Meta:
        model = Order2
        fields = '__all__'
