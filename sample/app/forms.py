from django import forms
from .models import User1
class User1Form(forms.ModelForm):
    class Meta:
        model=User1
        fields=['Fullname','email','address','mobile']
        # widgets = {'Fullname':forms.TextInput(attrs={'placeholder': 'Enter your name', 'style': 'margin-left: 3.3rem; padding-left: 1rem' ,'class':'form_control'}),
        #            'email': forms.TextInput(attrs={'placeholder': 'Enter your mail', 'style': 'margin-left: 3.4rem; padding-left: 1.3rem;padding-right:1.3rem', 'class': 'form_control'}),
        #            'address': forms.PasswordInput(attrs={'placeholder': 'Enter password', 'style': 'margin-left: 1.5rem; padding-left: 1rem','class': 'form_control'}),
        #            'mobile': forms.TextInput(attrs={'placeholder': 'Enter mobile', 'style': 'margin-left: 1.5rem; padding-left: 1rem','class': 'form_control'})
        #            }