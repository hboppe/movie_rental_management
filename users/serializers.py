from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="username already taken.")
        ]
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")]
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"] == True:
            user = User.objects.create_superuser(**validated_data)
            return user
        
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():

            if(key == "password"):
                instance.set_password(value)

            else: 
                setattr(instance, key, value)
        instance.save()

        return instance
