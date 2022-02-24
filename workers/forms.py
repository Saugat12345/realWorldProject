from django.forms import ModelForm
from .models import Worker, AppliedWorker

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
class AppliedWorkerForm(ModelForm):
    class Meta:
        model = AppliedWorker
        fields = '__all__'





