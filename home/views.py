from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.forms import textForm
from Putext.utils import render_to_pdf
from home.models import Post


class home(TemplateView):
    template_name = 'forms.html'

    #Method to create the html form
    def get(self, request):
        form = textForm()
        args = {'form' : form }
        return render(request, self.template_name, args)


    # Method to render HTML template in the form of a pdf
    def post(self, request):
        form = textForm(request.POST)
        if form.is_valid():
            post_new = form.save(commit=False)
            post_new.save()

            title_new = form.cleaned_data['title']
            text_new = form.cleaned_data['text']
            form = textForm()
        args = { 'text':text_new, 'title':title_new}
        pdf = render_to_pdf('final_pdf.html', args)
        return HttpResponse(pdf, content_type = 'application/pdf')