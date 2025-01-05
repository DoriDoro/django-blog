from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField


def _user_directory_path(instance, filename):
    # Generate a path: media/images/users/<user_id>/<filename>
    return f"images/users/{instance.username}-{instance.id}/{filename}"


class User(AbstractUser):
    introduction = HTMLField(blank=True, null=True)
    photo = models.ImageField(upload_to=_user_directory_path, blank=True, null=True)
    can_be_contacted = models.BooleanField(blank=True, null=True)
    can_data_be_shared = models.BooleanField(blank=True, null=True)
    professions = models.ManyToManyField("Profession", related_name="users", blank=True)
    services = models.ManyToManyField("Service", related_name="users", blank=True)
    websites = models.ManyToManyField("Website", related_name="users", blank=True)


class Profession(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
