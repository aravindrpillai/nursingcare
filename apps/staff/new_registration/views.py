from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from apps.core.models import Credentials
from apps.staff.new_registration.serializer import NewStaffRegistrationSerializer
from rest_framework.views import APIView


class StaffNewRegistration(APIView):

    def get(self, request):
        if request.method == "GET":
            credentials = Credentials.objects.all()
            serialize_obj = NewStaffRegistrationSerializer(credentials)
            return JsonResponse(serialize_obj.data)
        else:
            raise Exception("Method not allowed")

    def post(self, request):
        self._validate(request)
        request_object = JSONParser().parse(request)
        self._create_new_staff(request_object)
        resp = {
            "status" : "success"
        }
        return JsonResponse(resp)

    def _validate(self, request):
        if request.method != "POST":
            raise Exception("This API support only POST method.")

    def _create_new_staff(self, data):
        credentials = Credentials()
        credentials.username = data['username']
        credentials.password = data['password']
        credentials.save()
