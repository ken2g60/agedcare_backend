from rest_framework import serializers
from health.models import HealthData
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
    