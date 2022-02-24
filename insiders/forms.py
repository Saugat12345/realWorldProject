from django.forms import ModelForm
from .models import Insider


class InsiderForm(ModelForm):
    class Meta:
        model = Insider
        fields = '__all__'

