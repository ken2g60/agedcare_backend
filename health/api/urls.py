from django.urls import path 
from health.api.views import HealthAPIView


urlpatterns = [
    path('api/v1/', HealthAPIView.as_view())
]
