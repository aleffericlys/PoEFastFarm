from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Essences, Oils, Scarabs
from .serializers import UserSerializer, EssencesSerializer, OilsSerializer, ScarabsSerializer

import jwt, datetime

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


def delete_user_essence(id):

	try:
		essence = Essences.objects.get(idEssences=id)
		essence.delete()
		return Response(status=status.HTTP_202_ACCEPTED)
	except Essences.DoesNotExist:
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

def delete_user_oil(id):

	try:
		oil = Oils.objects.get(oil_id=id)
		oil.delete()
		return Response(status=status.HTTP_202_ACCEPTED)
	except Oils.DoesNotExist:
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


def delete_user_scarab(id):

	try:
		scarab = Scarabs.objects.get(idScarabs=id)
		scarab.delete()
		return Response(status=status.HTTP_202_ACCEPTED)
	except Scarabs.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request):

	if request.method == 'GET':
		token = request.COOKIES.get('jwt')
	
		if not token:
			return Response({'message':'User not logged'},status=status.HTTP_401_UNAUTHORIZED)

		try:
			payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return Response(status=status.HTTP_401_UNAUTHORIZED)
		
		try:
			user = User.objects.get(email=payload['email'])
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		serializer = UserSerializer(user)

		return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

	# pegando usuário pelo nick com request.GET
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
	
	# criando novo usuário
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
			else:
				print(user_serializer.errors)
				return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	# atualizando usuário
	if request.method == 'PUT':

		email = request.data['email']

		try:
			user_data = User.objects.get(pk=email)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = UserSerializer(user_data, data=request.data)



		if serializer.is_valid():

			serializer.save()
			return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	# deletando usuário
	if request.method == 'DELETE':
		try:
			user = User.objects.get(pk=request.data['email'])

			delete_user_scarab(str(user.Scarabs_idScarabs))
			delete_user_oil(str(user.oils_oil_id))
			delete_user_essence(str(user.Essences_idEssences))

			user.delete()
			return Response(status=status.HTTP_202_ACCEPTED)
		except User.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):

	if request.method == 'POST':

		email = request.data['email']
		password = request.data['password']

		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			return Response({'message':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
		
		if not user.check_password(password):
			return Response({'message':'Incorrect Password'}, status=status.HTTP_401_UNAUTHORIZED)
		
		payload = {
			'email': user.email,
			'exp': datetime.datetime.now() + datetime.timedelta(days=1),
			'iat': datetime.datetime.now()
		}

		token = jwt.encode(payload=payload, key='secret', algorithm='HS256')

		response = Response({'jwt': token}, status=status.HTTP_202_ACCEPTED)
		response.set_cookie(key='jwt', value=token, httponly=True)

		return response


@api_view(['POST'])
def user_logout(request):
	
	if request.method == 'POST':

		response = Response({'mensage': 'successful logout'}, status=status.HTTP_202_ACCEPTED)
		response.delete_cookie('jwt')

		return response


# @api_view(['POST'])
# def teste(request):

# 	if request.method == 'POST':

# 		new_user = request.data
# 		serializer = UserSerializer(data = new_user)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)

# 	return Response(status=status.HTTP_400_BAD_REQUEST)	


@api_view(['DELETE'])
def delete_scarab(request, id):
	if request.method == 'DELETE':
		try:
			scarab = Scarabs.objects.get(idScarabs=id)
			scarab.delete()
			return Response(status=status.HTTP_202_ACCEPTED)
		except Scarabs.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		
@api_view(['DELETE'])
def delete_oil(request, id):
	if request.method == 'DELETE':
		try:
			oil = Oils.objects.get(oil_id=id)
			oil.delete()
			return Response(status=status.HTTP_202_ACCEPTED)
		except Oils.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		
@api_view(['DELETE'])
def delete_essence(request, id):
	if request.method == 'DELETE':
		try:
			essence = Essences.objects.get(idEssences=id)
			essence.delete()
			return Response(status=status.HTTP_202_ACCEPTED)
		except Essences.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)