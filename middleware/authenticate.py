from django.contrib import messages
from utils.app_util import AppUtil
from utils.logger import Logger
from utils.display_key import DisplayKey
from properties.session_properties import SessionProperties

'''
    Authentication Middleware
'''


class Authenticate():
    excluded_apps = [
        "admin","staff"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        app_name = AppUtil.getAppName(request)
        Logger.info("Triggering app : "+app_name)
        if app_name not in self.excluded_apps:
            user_id = request.session[
                SessionProperties.USER_ID_KEY] if SessionProperties.USER_ID_KEY in request.session else None
            if user_id is None:
                Logger.error("Middleware Authentication Denied User ID {} To Access App {} ".format(user_id, app_name))
                messages.warning(request, DisplayKey.get("error_session_time_out"))
                raise Exception("Access Denied.")

        return self.get_response(request)
