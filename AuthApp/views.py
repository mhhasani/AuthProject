from django.http.response import HttpResponse
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
from django.contrib.auth.decorators import login_required
import mimetypes
from Authentication.settings import BASE_DIR


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('edit-user-profile')
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
        profile = UserProfile.objects.filter(user=user)
        context = super().get_context_data(**kwargs)
        context["user"] = profile.get()
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


@login_required
def download_file(request, filepath, filename):
    # Define text file name
    filename = filename
    # Define the full file path
    filepath = BASE_DIR / f'Upload/{filepath}/{filename}'
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
