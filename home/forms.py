from django import forms

from home.models import Post


class textForm(forms.ModelForm):
    text_input = forms.CharField()
    
    class Meta:
        model = Post
        fields = ('text_input', )