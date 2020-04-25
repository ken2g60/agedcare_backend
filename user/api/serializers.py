from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    
    def create(self, validated_data):
        user = UserModel.objects.create(
            phonenumber=validated_data['phonenumber'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    class Meta:
        model = UserModel
        fields = ( "id", "phonenumber", "email", "password", )
        