from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from apps.users.models import EnUsers

User = get_user_model()

class EnUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnUsers
        fields = (
            'email_id',
            'gender',
            'mobile_number',
            'subscribe_for_updates',
            'date_of_birth',
            'full_name',
            'display_picture'
        )