from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .jwt import create_jwt, decode_jwt

from datetime import datetime, timedelta

from utils.mixins import CustomLoggingViewSetMixin

User = get_user_model()


class LoginView(CustomLoggingViewSetMixin, APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow()
        }

        token = create_jwt(payload)
        return Response({'jwt': token})


class ActivateUserEmailView(CustomLoggingViewSetMixin, APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, uidb64, token):

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(_('Thank you for your email confirmation. Now you can login your account.'), status=HTTP_204_NO_CONTENT)
        else:
            return Response(_('Activation link is invalid!'), status=HTTP_204_NO_CONTENT)
