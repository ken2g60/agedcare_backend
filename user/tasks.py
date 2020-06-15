from celery.decorators import task
from user.models import Payment, Subscription
sms = SMS(client_id="", client_secret="")
from sentry_sdk import capture_exception, capture_message


import datetime
from datetime import timedelta