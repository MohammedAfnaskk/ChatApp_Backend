from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from rest_framework.serializers import ModelSerializer,SerializerMethodField

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_active'] = user.is_active
        token['is_google'] = user.is_google

        return token
    
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GoogleAuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name','last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }