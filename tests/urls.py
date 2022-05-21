from django.urls import re_path, include

from . import views


urlpatterns = [
    re_path(r'^$', views.test_jquery, name='lazy_tags_jquery'),
    re_path(r'^js/$', views.test_javascript, name='lazy_tags_javascript'),
    re_path(r'^prototype/$', views.test_prototype, name='lazy_tags_prototype'),
    re_path(r'^lazy_tags/', include('lazy_tags.urls')),
]
