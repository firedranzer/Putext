from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from .utils import render_to_pdf


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('final_pdf.html')
        context = {
            "invoice_id": 123,
            "customer_name": "Rupesh Harode",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('final_pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")