"""Users app models"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Inherits Django AbstractUsers and will be used ass project user model
    """

    email = models.EmailField(_("email address"), blank=True, unique=True)
