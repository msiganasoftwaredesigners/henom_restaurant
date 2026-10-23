import logging
import threading

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservationForm

logger = logging.getLogger(__name__)


def _send_notification(reservation):
    message = (
        f"New reservation details:\n\n"
        f"Name: {reservation.full_name}\n"
        f"Date: {reservation.date}\n"
        f"Time: {reservation.time}\n"
        f"Number of Persons: {reservation.number_of_person}\n"
        f"Meal: {reservation.get_meal_display()}\n"
        f"Email: {reservation.email}\n"
        f"Phone: {reservation.phone}\n\n"
        "Please check the reservation and prepare accordingly.\n\n"
        "Best regards,\n"
        "Henom Restaurant"
    )
    try:
        send_mail(
            'New Reservation Received',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['info@henomrestaurants.com'],
            fail_silently=False,
        )
    except Exception:
        logger.exception("Reservation %s saved but notification email failed", reservation.pk)


@csrf_exempt
def reservation_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            
            # Send the notification email in the background so a slow or
            # broken SMTP server can never hang the request (502/504).
            threading.Thread(
                target=_send_notification, args=(reservation,), daemon=True
            ).start()

            return JsonResponse({'message': 'Reservation successful!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})
