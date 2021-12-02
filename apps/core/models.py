from django.db import models


class Credentials(models.Model):
    username = models.CharField(max_length=25, unique=True, null=False)
    password = models.CharField(max_length=25, null=False)
    previous_password = models.CharField(max_length=25, null=True)
    last_login_time = models.DateField(null=True)
    failed_login_attempts = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        db_table = "credentials"


class Gender(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        managed = True
        db_table = "gender"


class District(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        managed = True
        db_table = "district"


class State(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        managed = True
        db_table = "state"


class Country(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        managed = True
        db_table = "country"


class Address(models.Model):
    house_name = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    district = models.ForeignKey(District, null=True, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=7, null=True)
    is_default_address = models.BooleanField(null=True)

    class Meta:
        managed = True
        db_table = "address"
