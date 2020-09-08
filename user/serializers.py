from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):

        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(email=email, username=username)
        # Sets the user’s password to the given raw string,
        # taking care of the password hashing. Doesn’t save the User object.

        user.set_password(password)

        # save() method to save the user object
        user.save()

        return user
