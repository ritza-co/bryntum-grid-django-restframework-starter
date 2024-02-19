from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=False)
    team = serializers.CharField(required=False)
    score = serializers.CharField(required=False)
    percentage_wins = serializers.CharField(required=False)

    class Meta:
        model = Player
        fields = ('id', 'name', 'city', 'team', 'score', 'percentage_wins')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if 'name' not in validated_data:
            validated_data['name'] = instance.name

        instance.save()
        return instance
