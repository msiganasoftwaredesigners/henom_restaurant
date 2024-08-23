from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservationForm

@csrf_exempt
def reservation_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            
            # Send an email notification to the restaurant
            subject = 'New Reservation Received'
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
            recipient_email = 'info@henomrestaurant.com'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            
            return JsonResponse({'message': 'Reservation successful!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})
