from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

class UserListView(ListView):

    model = models.UUIDUser
    paginate_by = 100  # if pagination is desired
    template_name = 'core/user/list.html'

class UserDetailView(DetailView):

    model = models.UUIDUser
    template_name = 'core/user/detail.html'