from django import forms


class textForm(forms.Form):
    text_input = forms.CharField()
    