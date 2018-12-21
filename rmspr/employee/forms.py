from django import forms
from models import *

class employee(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


class Meta:
    model = employee
    fields = ('employee_id','first_name','last_name','email','phone_no','password')