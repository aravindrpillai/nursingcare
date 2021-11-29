from django.db import models
from apps.core.models import Gender, Address, Credentials


# Staffs Data model
# Created on : 30 Nov 2021
class Staffs(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    display_picture = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, null=False)
    email_id = models.EmailField(null=True, unique=False)
    subscribe_for_updates = models.BooleanField(default=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    credential = models.ForeignKey(Credentials, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "en_staffs"
        verbose_name = "en_staffs"
