from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from Group.forms import GroupCreationForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import AccessMixin


class CreateGroupView(LoginRequiredMixin, View):
    def get(self, request):
        form = GroupCreationForm()
        return render(request, "CreateGroup.html", {'form': form})

    def post(self, request):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            form.save(user)
        else:
            return render(request, "CreateGroup.html", {'form': form})
        return redirect('my-groups')


class DeleteGroupView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        group = Group.objects.filter(pk=self.kwargs['pk'])
        if not group:
            return HttpResponse("group not found!")
        participant = Participant.objects.all().filter(user=user, group=group.get())
        role = "N"
        if participant:
            participant = participant.get()
            role = participant.role
        if role != "O":
            return HttpResponse("you can not delete this group!")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        group = Group.objects.filter(pk=self.kwargs['pk'])
        group.delete()
        return redirect('my-groups')


class MyGroupsListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'GroupList.html'

    def get_context_data(self, **kwargs):
        participants = Participant.objects.filter(
            user__pk=self.request.session['_auth_user_id'])
        context = super().get_context_data(**kwargs)
        context['participants'] = participants
        return context


class GroupDetailsView(LoginRequiredMixin, AccessMixin, DetailView):
    model = Group
    template_name = 'GroupDetails.html'

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        group = Group.objects.filter(pk=self.kwargs['pk'])
        participant = Participant.objects.all().filter(user=user, group=group.get())
        role = "N"
        if participant:
            participant = participant.get()
            role = participant.role
        if role == "N":
            return HttpResponse("group not found!")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        group = Group.objects.filter(pk=self.kwargs['pk'])
        participants = Participant.objects.filter(group__pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['participants'] = participants
        context['group'] = group.get()
        return context


class JoinGroupView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        group = Group.objects.all().filter(link=self.kwargs['link'])
        participant = Participant.objects.all().filter(
            user__pk=self.request.session['_auth_user_id'],
            group__link=self.kwargs['link'])
        if group:
            group = Group.objects.all().get(link=self.kwargs['link'])
            if not participant:
                participant = Participant.objects.create(
                    role='M',
                    user=user,
                    group=group,
                )
                participant.save()
            return redirect('group-details', group.pk)
        else:
            return HttpResponseNotFound("this link is not true!")
