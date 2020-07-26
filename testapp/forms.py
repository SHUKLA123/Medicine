from django import forms
from testapp.models import Sell1
from testapp.models import Buy1
from django.contrib.auth.models import User
from testapp.models import Upload_Prescription
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class Upload_pdf(forms.ModelForm):
    class Meta:
        model=Upload_Prescription
        fields=['prescrition',]

class Sell1Form(forms.ModelForm):
    class Meta:
        model=Sell1
        fields='__all__'

class Buy1Form(forms.ModelForm):
    class Meta:
        model=Buy1
        fields = '__all__'
