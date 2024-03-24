from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
from .modules.compute import compute


@csrf_exempt
def api(request):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)

            if len(data) == 4:
                cart_value, distance, items, time = float(data['cartValue']), int(
                    data['distance']), int(data['items']), data['time']

                if (type(cart_value) == float and type(distance) == int and type(items) == int and type(time) == str):
                    result = compute(cart_value, distance, items, time)
                    return JsonResponse(json.dumps({"delivery_fee": result}), safe=False)
                else:
                    return JsonResponse(json.dumps({"delivery_fee": "A parameter is of an invalid type."}), safe=False)
            else:
                return JsonResponse(json.dumps({"delivery_fee": f"Expected 4 parameters. Got {len(data)}."}), safe=False)
        else:
            return JsonResponse(json.dumps({"delivery_fee": "Parameters missing from request body."}), safe=False)
    else:
        return HttpResponseForbidden('Forbidden')
