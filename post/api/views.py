from post.models import Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostAPIView(APIView):
    
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)