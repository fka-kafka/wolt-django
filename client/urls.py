from django.urls import path
from .views import client

app_name = 'client'

urlpatterns = [
    path('', client, name='client')
]
