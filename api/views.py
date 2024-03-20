from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .modules.compute import compute


@csrf_exempt
def api(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        cartValue, distance, items, time = int(data['cartValue']), int(
            data['distance']), int(data['items']), data['time']

        result = compute(cartValue, distance, items, time)
        print(result)

        return HttpResponse(request.body)
    else:
        return HttpResponse('Forbidden')
