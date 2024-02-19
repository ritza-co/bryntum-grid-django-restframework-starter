from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'player_info', views.PlayerViewSet)

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += router.urls