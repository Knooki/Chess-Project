from django.contrib.auth.models import User, Group
from applications.quickstart.models import Player
from rest_framework import viewsets
from rest_framework import permissions
from applications.quickstart.serializers import UserSerializer, GroupSerializer, PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-date_joined')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
