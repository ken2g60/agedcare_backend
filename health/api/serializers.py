from rest_framework import serializers
from health.models import HealthData, Glucose, Pressure, Weight
from careapp.models import PersonalDetail

class HealthDataSerializer(serializers.Serializer):
    userId = serializers.CharField()
    phonenumber = serializers.CharField()
    bloodsugar = serializers.CharField()
    bloodpressure = serializers.CharField()
    bloodcholesterol = serializers.CharField()
    bloodlevel = serializers.CharField()
    weight = serializers.CharField()
    created_at = serializers.DateTimeField()
    
    
    def create(self, validated_data):
        return HealthData.objects.create(**validated_data)
    
    
class GlucoseSerializer(serializers.Serializer):
    userId = serializers.CharField()
    glucose = serializers.CharField()
    created_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Glucose.objects.create(**validated_data)


class PressureSerializer(serializers.Serializer):
    userId = serializers.CharField()
    systolic = serializers.CharField()
    diastolic = serializers.CharField()
    created_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Pressure.objects.create(**validated_data)


class WeightSerializer(serializers.Serializer):
    userId = serializers.CharField()
    weight = serializers.CharField()
    created_at = serializers.DateTimeField()
    
    
    def create(self, validated_data):
        return Weight.objects.create(**validated_data)