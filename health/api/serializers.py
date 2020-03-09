from rest_framework import serializers

from careapp.models import PersonalDetail

class PersonalDetailSerializer(serializers.Serializer):
    
    class Meta:
        model = PersonalDetail
        fields = ('__all__')
    
    def create(self, validated_data):
        pass