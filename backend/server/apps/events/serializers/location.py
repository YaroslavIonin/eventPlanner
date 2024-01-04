from rest_framework import serializers

from ..models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'address',
            'latitude',
            'longitude',
        )

    def create(self, validated_data: dict) -> Location:
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

