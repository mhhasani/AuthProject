from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from Group.forms import GroupCreationForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateGroupView(LoginRequiredMixin, View):
    # form_class = GroupCreationForm
    # success_url = reverse_lazy('my-groups')
    # template_name = 'CreateGroup.html'
    def get(self, request):
        form = GroupCreationForm()
        return render(request, "CreateGroup.html", {'form': form})

    def post(self, request):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            form.save(user)
        return render(request, "CreateGroup.html", {'form': form})


class MyGroupsList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'GroupList.html'

    def get_context_data(self, **kwargs):
        participants = Participant.objects.filter(
            user__pk=self.request.session['_auth_user_id'])
        context = super().get_context_data(**kwargs)
        context['participants'] = participants
        return context


class GroupDetails(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'GroupDetails.html'

    def get_context_data(self, **kwargs):
        participants = Participant.objects.filter(
            user__pk=self.request.session['_auth_user_id'])
        context = super().get_context_data(**kwargs)
        context['participants'] = participants
        group = Group.objects.get(pk=self.kwargs['pk'])
        context['group'] = group.name
        return context
