from django.conf.urls import url
from .views import checkout, donate

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^donate/', donate, name='donate'),
]
