from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.index_view.as_view(),name='index'),
    path('about',v.about_view.as_view(),name='about'),
    path('services',v.services_view.as_view(),name='services'),
    path('blogs',v.blogs_view.as_view(),name='blogs'),
    path('contact',v.contact_view.as_view(),name='contact'),
]