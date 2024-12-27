from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.index_view.as_view(),name='index_view'),
    path('about',v.about_view.as_view(),name='about_view'),
]