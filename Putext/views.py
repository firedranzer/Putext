from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response


def home(request): 
    return render_to_response('final_pdf.html')