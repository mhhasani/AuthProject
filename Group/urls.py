from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', MyGroupsListView.as_view(), name='my-groups'),
    path('Create-Group/', CreateGroupView.as_view(), name='create-group'),
    path('Delete-Group/<int:pk>/', DeleteGroupView.as_view(), name='delete-group'),
    path('<int:pk>/', GroupDetailsView.as_view(), name="group-details"),
    path('join/<str:link>/', JoinGroupView.as_view(), name='join-group'),
]
