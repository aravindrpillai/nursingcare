from django.db import models
from apps.core.models import EnCredentials

# Create your models here.
   
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
class EnUsers(models.Model): #db_table = en_users
    full_name            = models.CharField(max_length=100, null=True)
    display_picture      = models.CharField(max_length=100, null=True)
    date_of_birth        = models.DateField(null=True)
    gender               = models.IntegerField(choices=GENDER_CHOICES)
    mobile_number        = models.CharField(max_length=10, null=False)
    email_id             = models.EmailField(null=True, unique=False)
    subscribe_for_updates= models.BooleanField(default=True)
    credential           = models.ForeignKey(EnCredentials, null=True, on_delete=models.CASCADE)
    class Meta:
      verbose_name = "En_Users"

    def __str__(self):
        return self.username