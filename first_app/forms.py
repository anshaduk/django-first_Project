from django import forms
from django.core import validators
from first_app.models import Webpage

def value_starts_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError('Enter name starts with z!!!')
class FormName(forms.Form):
    name=forms.CharField(validators=[value_starts_z])
    email=forms.EmailField()
    verify_email=forms.EmailField(label='verify email')
    description=forms.CharField(widget=forms.Textarea)

class webpage1(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'