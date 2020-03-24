from django.urls import path 
from post.api.views import PostAPIView


urlpatterns = [
    path('post/', PostAPIView.as_view())
]
