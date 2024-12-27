from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView


def my_index (request):
    return render (request, 'index.html')

def my_about (request):
    return render (request, 'about.html')

def my_hello (request):

    txt_result='Hello Django'

    return HttpResponse (txt_result)

def welcome(request):
    user_name='Suphi Çakır'

    return render (request,'welcome.html',{'user_name':user_name})

def website_info(request):

    context_data={
        'var_full_name':'Suphi Çakır',
        'var_e_mail':'suphicakir@gmail.com',
        'var_website':'www.google.com',
    }

    return render(request,'website_info.html', context_data )

def category_details_view (request,category_slug):

    return render(request, 'category_details.html', {'category_details':category_slug})

def category_details_view_with_id (request,category_id):

    return render(request, 'category_id.html', {'category_id':category_id})

def category_details_view_with_name (request,category_name):

    return render(request, 'category_name.html', {'category_name':category_name})

def yonlendir (request):
    return redirect('https://www.google.com')

class index_view (TemplateView):
    template_name='index.html'


class test_views(TemplateView):
    template_name='test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World'
        return context