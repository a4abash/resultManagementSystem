from django import forms
from .models import Manager
from student.models import Result, Student


class Addresult(forms.ModelForm):
    rts = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    se = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    compiler = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    webtech = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    imgprcss = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Result
        exclude = []
