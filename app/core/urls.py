from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as core
from . import api_views as api

app_name = 'core'

urlpatterns = [

    # Users
    path('usuarios/', core.UserListView.as_view(), name='users-list'),
    path('usuarios/<uuid:pk>/', core.UserDetailView.as_view(), name='user-detail'),
    
]
