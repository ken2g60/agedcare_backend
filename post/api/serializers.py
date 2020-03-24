from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.FileField()
    created_at = serializers.DateTimeField()