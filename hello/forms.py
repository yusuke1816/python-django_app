from django import forms
class SessionForm(forms.Form):
  session = forms.CharField(label='session', required=False, \
    widget=forms.TextInput(attrs={'class':'form-control'}))
