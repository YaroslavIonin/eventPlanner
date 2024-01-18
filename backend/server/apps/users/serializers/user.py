from rest_framework import serializers

from ..models import User
from ..serializers import ChildSerializer
from apps.events.serializers import LocationSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


class UserSummarySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source="user.email",
        required=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True)
    locations = LocationSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'children',
            'locations'
        )
