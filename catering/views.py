from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CateringForm

@csrf_exempt
def catering(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = CateringForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Reservation successful!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = CateringForm()
    return render(request, 'catering.html', {'form': form})
