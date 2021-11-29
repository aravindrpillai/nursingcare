from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated   
from rest_framework.response import Response

from apps.users.models  import EnUsers
from apps.users.api.serializer import EnUserSerializer


class EnUserViewSet(APIView):

    permission_classes = (IsAuthenticated,)   

    def post(self, request):
        serializer = EnUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(credential=request.user)
        return Response({"status": status.HTTP_200_OK})


class CreateUserView(APIView):
        model = EnUsers
        serializer_class = EnUserSerializer

        def get(self, request):
            user = self.request.user
            serializer = EnUserSerializer(EnUsers.objects.filter(credential=user),many=True)
            return Response(serializer.data)