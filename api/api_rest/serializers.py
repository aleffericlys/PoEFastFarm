from rest_framework import serializers

from .models import User, Essences, Oils, Scarabs

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['email', 'name', 'nickName', 'password', 'profilePicture','Essences_idEssences', 'oils_oil_id', 'Scarabs_idScarabs']
		# fields = '__all__'
	
	def update(self, instance, validated_data):

		validated_data.pop('Essences_idEssences', None)
		validated_data.pop('oils_oil_id', None)
		validated_data.pop('Scarabs_idScarabs', None)
		validated_data.pop('createdAt', None)

		return super().update(instance, validated_data)

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