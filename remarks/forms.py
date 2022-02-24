from django.forms import ModelForm
from .models import Remark


class RemarkForm(ModelForm):
    class Meta:
        model = Remark
        fields = '__all__'
