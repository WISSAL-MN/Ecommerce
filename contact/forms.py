from django import forms
from .models import Contact

# Create your models here.
class ContactModelForm(forms.ModelForm) :
    class Meta : 
        model = Contact
        fields=[
            'name',
            'title',
            'email'
            'description'
        ]