from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from AuthApp.models import UserProfile
from random import randint
from django.core.validators import MinLengthValidator


def create_random_link():
    final = ''
    li = 'abcdefghijklmnopqrstuxwzy1234567890'
    for i in range(1, 16):
        random_index = randint(1, 34)
        final += li[random_index]
    return final


class Group(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=15, validators=[
                            MinLengthValidator(5)], default=create_random_link(), null=True)


class Participant(models.Model):
    ROLE_CHOICE = (
        ("O", "Owner"),
        ("A", "Admin"),
        ("M", "Member"),
    )
    role = models.CharField(max_length=6, choices=ROLE_CHOICE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
