from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AuthApp.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def save(self, user=None):
        user_profile = super().save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email",)
