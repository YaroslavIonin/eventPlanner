from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..serializers import UserProfileSerializer


class UserProfilePIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self) -> User:
        return self.request.user
