from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import Player
from .serializers import PlayerSerializer
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)["data"]
            created_players = []
            for record in data:
                del record["id"]
                serializer = self.get_serializer(data=record)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                created_players.append(serializer.data)
            return Response({'success': True, 'data': created_players}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['PATCH'])
    def patch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)["data"]
            updated_players = []
            for record in data:
                partial = kwargs.pop('partial', True)
                try:
                    instance = self.queryset.get(id=record.get('id'))
                    serializer = self.get_serializer(instance, data=record, partial=partial)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                    updated_players.append(serializer.data)
                except Player.DoesNotExist:
                    continue
            return Response({'success': True, 'data': updated_players}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['DELETE'])
    def delete(self, request, *args, **kwargs):
        try:
            ids_to_delete = request.data.get('ids', [])
            instances_to_delete = self.queryset.filter(pk__in=ids_to_delete)
            instances_to_delete.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
