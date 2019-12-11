from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from agedcare_ussd.views import Hubtel, AfricaTalking

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'hubtel/', Hubtel.as_view()),
	url(r'africatalking/', AfricaTalking.as_view()),
]
