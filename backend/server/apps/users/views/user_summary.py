from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import User
from ..serializers import UserProfileSerializer, UserSummarySerializer


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self) -> User:
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(user, validated_data=serializer.validated_data)
            return Response(
                UserProfileSerializer(user).data
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
