from rest_framework import serializers
from apps.core.models import Credentials


class NewStaffRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ('username', 'password')
