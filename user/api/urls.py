from .views import CreateUserView
from django.urls import include, path


urlpatterns = [
    path("signup", CreateUserView.as_view(),name="signup"),
]