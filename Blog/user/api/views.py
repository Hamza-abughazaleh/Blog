from django.contrib.auth import login, logout
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user.api.serializer import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    # API for retail user login
    def post(self, request):
        self.ser = self.serializer_class(data=request.data)
        if self.ser.is_valid():
            self.user = self.ser.instance
            login(request, self.user)
            # refuse to login logged in users, to avoid attaching sessions to
            # multiple users at the same time.
            if request.user.is_authenticated:
                return Response(
                    {'detail': 'Session is in use, log out first'},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)

            return Response("ok")

        return Response(self.ser.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request):
        request = request._request
        if request.user.is_anonymous:
            return Response(
                {'detail': 'You Must Login First'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        logout(request)
        request.session.clear()
        request.session.delete()

        return Response("ok")
