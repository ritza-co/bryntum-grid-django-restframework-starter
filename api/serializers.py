from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=False)
    team = serializers.CharField(required=False)
    score = serializers.IntegerField(required=False)
    percentage_wins = serializers.IntegerField(required=False)

    class Meta:
        model = Player
        fields = ('id', 'name', 'city', 'team', 'score', 'percentage_wins')
