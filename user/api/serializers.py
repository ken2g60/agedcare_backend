from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

from user.models import Payment, Subscription

# asoriba payment
from utils.asoriba import Asoriba


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    
    def create(self, validated_data):
        user = UserModel.objects.create(phonenumber=validated_data['phonenumber'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    class Meta:
        model = UserModel
        fields = ( "id", "phonenumber", "email", "password")

# class SubscriptionSerializer(serializers.Serializer):
#     class Meta:
#         model = Subscription
#         fields = ("subscription_type",)
    
    
class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phonenumber = serializers.CharField()
    email = serializers.EmailField(allow_null=True)
    
    
    class Meta:
        model = Payment
        fields = ("amount", "first_name", "last_name", "phonenumber", "email")
        
    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)