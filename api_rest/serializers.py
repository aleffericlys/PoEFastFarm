from rest_framework import serializers

from .models import User, Essences, Oils, Scarabs

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class EssencesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Essences
		fields = '__all__'

class OilsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Oils
		fields = '__all__'

class ScarabsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scarabs
		fields = '__all__'