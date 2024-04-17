from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from api_layer.serializers import (
    UserSerializer,
)


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class ObtainAuthTokenView(ObtainAuthToken):
    renderer_classes = APIView.renderer_classes

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
