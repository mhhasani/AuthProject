from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import FormView
from AuthApp.forms import UserProfileForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import *


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class NewUserProfileView(FormView):
    template_name = "profile.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("home")


class EditUserProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("home")


def Home(request):
    is_authenticated = request.user.is_authenticated
    if is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
    else:
        user = None
    if UserProfile.objects.filter(user=user):
        profile = UserProfile.objects.get(user=user)
    else:
        profile = None
    context = {"is_authenticated": is_authenticated,
               "user": request.user, "profile": profile}
    return render(request, "Home.html", context)
