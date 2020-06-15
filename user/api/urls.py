from .views import CreateUserView, PaymentAPIView
from django.urls import include, path
from . import views 

urlpatterns = [
    path("signup", CreateUserView.as_view(),name="signup"),
    path("payment", PaymentAPIView.as_view(), name="payment"),
    path("webhook", views.webhook, name="webhook"),
]