from abc import ABC

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from apps.core.models import EnCredentials

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnCredentials
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = EnCredentials(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializers(serializers.Serializer, ABC):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
