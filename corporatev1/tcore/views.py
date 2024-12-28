from django.views.generic import TemplateView

class index_view(TemplateView):
    template_name = 'index.html'

class about_view(TemplateView):
    template_name = 'about.html'


class services_view(TemplateView):
    template_name = 'services.html'


class blogs_view(TemplateView):
    template_name = 'blogs.html'

class contact_view(TemplateView):
    template_name = 'contact.html'
