from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def client(request):
  return render(request, 'app.html')