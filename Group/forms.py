from django import forms
from django.forms import fields
from .models import *


class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('__all__')

    def save(self, user):
        group = super().save(commit=False)
        group.save()
        participant = Participant.objects.create(
            role='O',
            user=user,
            group=group,
        )
        participant.save()
        return group
