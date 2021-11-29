from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class EnCredentials(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True, null=True)
    password = models.CharField(max_length=25, null=True)
    previous_password = models.CharField(max_length=25, null=True)
    last_login_time = models.DateField(null=True)
    failed_login_attempts = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "En_Credentials"

    def __str__(self):
        return self.username
