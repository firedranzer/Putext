from django.shortcuts import render
from forms import textForm

# Create your views here.
def home(request):
    return render(request,"forms.html",{ "form" : form })