from django.forms import ModelForm
from .models import Automobile, AppliedAutomobile


class AutomobileForm(ModelForm):
    class Meta:
        model = Automobile
        fields = '__all__'


class AppliedAutomobileForm(ModelForm):
    class Meta:
        model = AppliedAutomobile
        fields = '__all__'


