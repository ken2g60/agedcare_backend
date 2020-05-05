from celery import shared_task

@shared_task
def weekly_notification():
    # select phonenumber 
    # pressure and the glucose and weight
    print("weekly notitifcation")


@shared_task
def monthly_notification():
    print("monthly notification")
