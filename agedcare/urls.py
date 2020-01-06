from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from agedcare_ussd.views import Hubtel, AfricaTalking

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "AgedCare Admin"
admin.site.site_title = "AgedCare"
admin.site.index_title = "Welcome to AgedCare Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'hubtel/', Hubtel.as_view()),
	url(r'africatalking/', AfricaTalking.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
