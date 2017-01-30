from collections import defaultdict
import hashlib
import platform
import random
import math


from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from assignment.models import ShortUrl
from rest_framework import viewsets, status
from rest_framework.response import Response
from assignment.serializers import UserSerializer, ShortenedUrlSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ShortenedUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all().order_by('pk')
    serializer_class = ShortenedUrlSerializer

    def list(self, request, **kwargs):
        """
        List all Short URLs

        :return:
        """
        url_list = []
        queryset = ShortUrl.objects.all().order_by('pk')
        for obj in queryset:
            request_url = 'http://' + request.environ["HTTP_HOST"]
            request_path = request.path
            complete_url = request_url + request_path + str(obj.short_url)
            url_list.append({'url': complete_url,
                             'Last Checked': obj.last_checked,
                             'Views': obj.no_of_views})

        return Response({'status': 'OK',
                         'Results': url_list
                         }, status.HTTP_200_OK)

    def create(self, request):
        """
        Create new short url

        :return:
        """
        try:
            url = request.data["long_url"]
            print url
            if not url:
                return {"success": False, "message": "Invalid URL"}

            try:
                obj = ShortUrl.objects.get(long_url=url)
            except ShortUrl.DoesNotExist:
                obj = get_unique_id(url)

            return Response({"success": True, "url": "http://%s/%s" % ('127.0.0.1:8000/api', obj.short_url), "edit_url": "/edit/%s" % obj.short_url })
        except:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, **kwargs):
        try:
            if pk:
                instance = get_object_or_404(ShortUrl, short_url=pk)
                instance.no_of_views += 1
                instance.save()
                if 'http://' not in instance.redirect_location:
                    instance.redirect_location = 'http://'+instance.redirect_location
                return HttpResponseRedirect(instance.redirect_location)

        except:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)


def get_unique_id(url):
    """ Return new (saved) Url object with unique short URL """
    iteration = 0
    hdigest = "%s-%s" % (url, random.random())
    while True:
        hdigest = hashlib.sha512(hdigest).hexdigest()
        if iteration < 10:
            short_url = hdigest[0:4]
        else:
            length = 4 + int(math.sqrt(iteration - 10))
        if iteration == 100:
            raise Exception("Can't find unique shorturl")
        try:
            obj = ShortUrl.objects.create(short_url=str(short_url), redirect_location=url)
            obj.save()
            return obj
        except IntegrityError:
            iteration += 1
