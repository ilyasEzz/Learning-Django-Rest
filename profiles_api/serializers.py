from rest_framework import serializers

from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'login', 'name', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create a new user """

        user = UserProfile.objects.create_user(
            login=validated_data['login'],
            password=validated_data['password'],
            name=validated_data['name'],
        )

        return user
