from django.conf.urls import url, include
from .views import all_gifts


urlpatterns = [
    url(r'^$', all_gifts, name='gifts')
]
