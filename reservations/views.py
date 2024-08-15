from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservationForm

@csrf_exempt
def reservation_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Reservation successful!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})
