from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .functions import essence, oil


@api_view(['GET'])
def essences(request):

	essenceItens = essence()

	return Response(essenceItens, status=status.HTTP_200_OK)


@api_view(['GET'])
def oils(request):
	
	oilItens = oil()

	return Response(oilItens, status=status.HTTP_200_OK)