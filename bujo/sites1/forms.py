from django import forms

class IndexCardForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=20)