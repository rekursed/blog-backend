from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.conf import settings

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.


@api_view(['GET'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def getAll(request, format=None):
    """
    Get all blogs
    """
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @renderer_classes([JSONRenderer, BrowsableAPIRenderer])
# def getCountries(request, format=None):
#     """
#     Gets country wise stats for all countries
#     """
#     result = dict()
#     try:
#         response = requests.get(settings.COVID_SOURCE_URL)
#         soup = BeautifulSoup(response.text, "html.parser")
#         countryTable = soup.findAll("table", {"id": 'main_table_countries_today'})
#
#
#         result["cases"] = int(re.sub("[ ,.]", "", counters[0].span.string))
#         result["deaths"] = int(re.sub("[ ,.]", "", counters[1].span.string))
#         result["recovered"] = int(re.sub("[ ,.]", "", counters[2].span.string))
#         result["updated_at"] = datetime.now()
#
#     except:
#         print('error occered')
#
#     return Response(result)