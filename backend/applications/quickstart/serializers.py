from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSericalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userfields = ['url', 'usernmae', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groupfields = ['url', 'name']