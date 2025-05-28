# orders/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(user_email, order_id):
    subject = "Order Confirmation"
    message = f"Thank you for your order!\nYour Order ID is {order_id}. We'll deliver your food shortly!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {user_email} for order {order_id}"
