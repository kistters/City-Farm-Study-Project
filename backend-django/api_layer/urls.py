from django.urls import path

from api_layer.views import (
    LogoutView, ObtainAuthTokenView, RegisterView,
)

urlpatterns = [
    path('obtain-auth-token/', ObtainAuthTokenView.as_view(), name='obtain-auth-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
