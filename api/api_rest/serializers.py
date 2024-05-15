from rest_framework import serializers

from .models import User, Essences, Oils, Scarabs

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['email', 'name', 'nickName', 'password', 'profilePicture', 'Essences_idEssences', 'oils_oil_id', 'Scarabs_idScarabs']
		extra_kwargs = {
			'name': {'required': False},
			'password': {'required': False},
            'Essences_idEssences': {'required': False},
            'oils_oil_id': {'required': False},
            'Scarabs_idScarabs': {'required': False},
        }
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