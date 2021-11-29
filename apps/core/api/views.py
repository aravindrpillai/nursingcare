from django.contrib.auth import login

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.models import EnCredentials
from apps.core.api.serializer import UserSerializer, LoginSerializers


class UserCreate(generics.CreateAPIView):
    queryset = EnCredentials.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})
