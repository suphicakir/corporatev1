from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views.generic import TemplateView


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
        if view:
            translation.activate(language)
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        else:
            response = HttpResponseRedirect("/")
        return response


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
