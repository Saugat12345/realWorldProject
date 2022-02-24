from django.forms import ModelForm
from .models import MyAdmin


class MyAdminForm(ModelForm):
    class Meta:
        model = MyAdmin
        fields = '__all__'
