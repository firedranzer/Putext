from django import forms

from home.models import Post


class textForm(forms.ModelForm):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    
    class Meta:
        model = Post
        fields = ('title', 'text',)