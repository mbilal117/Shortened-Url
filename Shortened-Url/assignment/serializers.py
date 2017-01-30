__author__ = 'ansbilal'

from django.contrib.auth.models import User
from rest_framework import serializers
from assignment.models import ShortUrl


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ShortenedUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('pk', 'url')
