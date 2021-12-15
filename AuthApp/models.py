from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from Authentication.settings import BASE_DIR


def path_and_rename(instance, filename):
    upload_to = 'ProfilePhoto'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.pk, ext)
    path = BASE_DIR / f"Upload/ProfilePhoto/{filename}"
    try:
        os.remove(path)
    except:
        pass
    return os.path.join(upload_to, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True)
