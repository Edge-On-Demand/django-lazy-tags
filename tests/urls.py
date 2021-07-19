from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.test_jquery, name='lazy_tags_jquery'),
    url(r'^js/$', views.test_javascript, name='lazy_tags_javascript'),
    url(r'^prototype/$', views.test_prototype, name='lazy_tags_prototype'),
    url(r'^lazy_tags/', include('lazy_tags.urls')),
]
