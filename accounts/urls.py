from django.conf.urls import url, include
from accounts.views import logout, login, registration, view_profile, edit_profile
from accounts import url_reset


urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', view_profile, name="view_profile"),
    url(r'^profile/edit/$', edit_profile, name="edit_profile"),
    url(r'^password-reset/', include(url_reset))
]
