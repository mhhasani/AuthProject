from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    url('profile/', EditUserProfileView.as_view(), name="edit-user-profile"),
]
