from django.urls import include, path


from .views import CreateUserView

urlpatterns = [
    path("signup", CreateUserView.as_view(),name="signup"),
]

