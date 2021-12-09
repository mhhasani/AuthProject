from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from AuthApp.forms import UserProfileForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile.html"

    def get_object(self, *args, **kwargs):
        user = User.objects.all().get(pk=self.request.session['_auth_user_id'])
        try:
            profile = UserProfile.objects.get(user=user)
        except:
            profile = UserProfile.objects.create(user=user)
            profile.save()
        return user.userprofile

    def get_context_data(self, **kwargs):
        user = User.objects.all().get(pk=self.request.user.pk)
        context = super().get_context_data(**kwargs)
        context["username"] = user.username
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse("home")


class Home(View):
    def get(self, request):
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
