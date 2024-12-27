from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.my_index, name='index'),
    path('about',v.my_about, name='about'),
    path('hello',v.my_hello, name='hello'),
    path('welcome',v.welcome,name='welcome'),
    path('website_info',v.website_info, name='website_info'),
    path('category/<slug:category_slug>/', v.category_details_view,name='category_detail'),
    path('category_id/<int:category_id>/', v.category_details_view_with_id,name='category_id'),
    path('category_name/<str:category_name>/', v.category_details_view_with_name,name='category_name'),
    path('yonlendir',v.yonlendir, name='yonlendir'),
    path('index',v.index_view.as_view(),name='index_view'),
    path('test',v.test_views.as_view(),name='test'),
]