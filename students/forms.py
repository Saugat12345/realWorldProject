from django import forms
from .models import Student, AppliedStudent

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class AppliedStudentForm(forms.ModelForm):
    class Meta:
        model = AppliedStudent
        fields = '__all__'