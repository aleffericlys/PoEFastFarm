from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Essences, Oils, Scarabs
from .serializers import UserSerializer, EssencesSerializer, OilsSerializer, ScarabsSerializer

import json

# Create your views here.
