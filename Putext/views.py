from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from Putext.utils import render_to_pdf
from home.views import home
from home.forms import textForm
from home.models import Post


class GeneratePDF(View):
    #template_name = 'final_pdf.html'
    def get(self, request, *args, **kwargs):
        template = get_template('final_pdf.html')
        #context = {
        #    "invoice_id": 123,
        #    "customer_name": "Rupesh Harode",
        #    "amount": 1399.99,
        #    "today": "Today",
        #}
        #html = template.render(Post)
        post = Post.objects.reverse()[0]
        pdf = render_to_pdf('final_pdf.html', {'post':post})
        return HttpResponse(pdf, content_type = 'application/pdf')


