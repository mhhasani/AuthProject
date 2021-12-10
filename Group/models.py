from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from AuthApp.models import UserProfile


class Group(models.Model):
    name = models.CharField(max_length=100)


class Participant(models.Model):
    ROLE_CHOICE = (
        ("O", "Owner"),
        ("A", "Admin"),
        ("M", "Member"),
    )
    role = models.CharField(max_length=6, choices=ROLE_CHOICE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
