from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', MyGroupsList.as_view(), name='my-groups'),
    path('Create-Group/', CreateGroupView.as_view(), name='create-group'),
    path('<int:pk>/', GroupDetails.as_view(), name="group-details"),
]
