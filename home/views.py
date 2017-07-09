from django.shortcuts import render
from .forms import textForm

# Create your views here.
def home(request):
    form = textForm
    return render(request,"forms.html",{ "form" : form } )