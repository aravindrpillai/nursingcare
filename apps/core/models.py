from django.db import models


class Credentials(models.Model):
    username = models.CharField(max_length=25, unique=True, null=False)
    password = models.CharField(max_length=25, null=False)
    previous_password = models.CharField(max_length=25, null=True)
    last_login_time = models.DateField(null=True)
    failed_login_attempts = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = "en_credentials"
        verbose_name = "en_credentials"

    def __str__(self):
        return self.username


class Gender(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        db_table = "tl_gender"
        verbose_name = "tl_gender"


class District(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        db_table = "tl_district"
        verbose_name = "tl_district"


class State(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        db_table = "tl_state"
        verbose_name = "tl_state"


class Country(models.Model):
    name = models.CharField(max_length=30, null=False)
    code = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    priority = models.IntegerField(null=False, default=10)

    class Meta:
        db_table = "tl_country"
        verbose_name = "tl_country"


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
        db_table = "en_address"
        verbose_name = "en_address"
