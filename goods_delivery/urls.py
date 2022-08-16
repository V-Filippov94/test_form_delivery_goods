from django.urls import path
from .views import *


urlpatterns = [
    path('', ShowFormDelivery.as_view(), name='form_delivery'),
]
