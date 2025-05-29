from django import forms

class HelloForm(forms.Form):
  mail = forms.EmailField(label='mail', \
    widget=forms.EmailInput(attrs={'class':'form-control'}))

