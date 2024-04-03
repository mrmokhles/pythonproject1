from django import forms
from app1.models import contactEnquiry
from .models import CountryGDP

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = contactEnquiry
        fields = ["name","email"]

class PersonForm(forms.ModelForm):
    
    class Meta:
        model =CountryGDP
        fields = '__all__'