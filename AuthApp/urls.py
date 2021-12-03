from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', Home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    url(r'^profiles/new/$', NewUserProfileView.as_view(), name="new-user-profile"),
    url(r'^users/(?P<pk>\d+)/edit/$',
        EditUserProfileView.as_view(), name="edit-user-profile"),
]
