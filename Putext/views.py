from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from Putext.utils import render_to_pdf
from home.views import home
from home.forms import textForm
from home.models import Post


class GeneratePDF(View):
    posts = Post.objects.all()
    template_name = 'final_pdf.html'
    def get(self, request, *args, **kwargs):
        template = get_template('final_pdf.html')
        #context = {
        #    "invoice_id": 123,
        #    "customer_name": "Rupesh Harode",
        #    "amount": 1399.99,
        #    "today": "Today",
        #}
        #html = template.render(Post)
        pdf = render_to_pdf('final_pdf.html', {'Post':Post})
        return HttpResponse(pdf, content_type = 'application/pdf')

    def post(self, request):
        form = textForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_input']
        
        args = { 'form': form, 'text': text}
        pdf = render_to_pdf(self.template_name, args)

