from rest_framework import serializers

from ..models import Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'name')

    def create(self, validated_data):
        validated_data['parent'] = self.context['request'].user
        return super().create(validated_data)
