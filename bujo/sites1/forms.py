from django import forms

class NameForm(forms.Form):
    fname = forms.CharField(label='name', max_length=20)