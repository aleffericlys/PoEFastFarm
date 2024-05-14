from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Essences, Oils, Scarabs
from .serializers import UserSerializer, EssencesSerializer, OilsSerializer, ScarabsSerializer

import json

# Create your views here.
@api_view(['GET'])
def get_users(request):

	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_escences(request, nick):

	if request.method == 'GET':

		try:
			user = User.objects.get(nickName=nick)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try:
			escences = Essences.objects.get(idEssences = str(user.Essences_idEssences))
		except Essences.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		serializer = EssencesSerializer(escences)
		return Response(serializer.data)
	
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_oils(request, nick):

	if request.method == 'GET':

		try:
			user = User.objects.get(nickName=nick)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try:
			oils = Oils.objects.get(oil_id = str(user.oils_oil_id))
		except Oils.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		serializer = OilsSerializer(oils)
		return Response(serializer.data)
	
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_scarabs(request, nick):

	if request.method == 'GET':

		try:
			user = User.objects.get(nickName=nick)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try:
			scarabs = Scarabs.objects.get(idScarabs = str(user.Scarabs_idScarabs))
		except Scarabs.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		serializer = ScarabsSerializer(scarabs)
		return Response(serializer.data)
	
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users_by_nick(request, nick):

	try:
		user = User.objects.get(nickName=nick)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

	if request.method == 'GET':

		try:
			if request.GET['user']:
				
				nick = request.GET['user']
				
				try:
					user = User.objects.get(nickName=nick)
				except User.DoesNotExist:
					return Response(status=status.HTTP_404_NOT_FOUND)
				
				serializer = UserSerializer(user)
				return Response(serializer.data)
			
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
	

	if request.method == 'POST':

		essence_serializer = EssencesSerializer(data = {})
		oil_serializer = OilsSerializer(data = {})
		scarab_serializer = ScarabsSerializer(data = {})

		if essence_serializer.is_valid() and oil_serializer.is_valid() and scarab_serializer.is_valid():
			essence_serializer.save()
			oil_serializer.save()
			scarab_serializer.save()

			new_user = request.data
			new_user['Essences_idEssences'] = essence_serializer.data['idEssences']
			new_user['oils_oil_id'] = oil_serializer.data['oil_id']
			new_user['Scarabs_idScarabs'] = scarab_serializer.data['idScarabs']

			user_serializer = UserSerializer(data = new_user)

			if user_serializer.is_valid():
				user_serializer.save()
				return Response(user_serializer.data, status=status.HTTP_201_CREATED)


		return Response(status=status.HTTP_400_BAD_REQUEST)
	





@api_view(['POST'])
def teste(request):

	if request.method == 'POST':

		new_user = request.data
		serializer = UserSerializer(data = new_user)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

	return Response(status=status.HTTP_400_BAD_REQUEST)	