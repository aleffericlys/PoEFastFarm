from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .functions import Essence


@api_view(['GET'])
def essences(request):
	essenceItens = Essence.filter_essence_type()
	return Response(essenceItens, status=status.HTTP_200_OK)