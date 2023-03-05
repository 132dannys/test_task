from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import (
    VendorCodeAPIView,
) 

urlpatterns = [
    path('api/v1/vendor-codes/', VendorCodeAPIView.as_view(), name='vendor-code'),
]
