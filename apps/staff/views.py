from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterStaff(APIView):
    def post(self, request, *args, **kwargs):
        data= {
            'username':'aravind',
            'age':20
        }
        return Response(data)
