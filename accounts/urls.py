from django.conf.urls import url
from accounts.views import logout, login, registration, view_profile


urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', view_profile, name="profile")
]
