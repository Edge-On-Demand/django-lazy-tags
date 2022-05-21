from django.urls import re_path

from .views import tag


urlpatterns = [
    re_path(r'^tag/(?P<tag_id>.+)?$', tag, name='lazy_tag'),
]
