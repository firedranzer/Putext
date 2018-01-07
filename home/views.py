from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from home.forms import textForm
from home.models import Post


class home(TemplateView):
    template_name = 'forms.html'

    def get(self, request):
        form = textForm()
        posts = Post.objects.all()[::-6]
        args = {'form' : form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self,request):
        form = textForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            text = form.cleaned_data['text_input']
            form = textForm()
            #return redirect('forms:forms')
        args = { 'form':form, 'text':text}
        return render(request, self.template_name, args)