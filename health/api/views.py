from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from health.api.serializers import HealthDataSerializer
from health.models import HealthData


class PersonalDetailsAPIView(APIView):
    
    def get(self, request):
        pass
    
    def post(self, request, *args, **kwargs):
        pass
    

class HealthAPIView(APIView):
    
    def get(self, request):
        health = Health.objects.all()
        # query user_id
    
    
    def post(self, request, *args, **kwargs):
        serializer = HealthDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        