from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        date_of_birth = validated_data.get('date_of_birth')
        user = User(
            email = email,
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save()
        return user