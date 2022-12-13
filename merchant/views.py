from django.shortcuts import render

from .serializers import MerchantProfileSerializer
from rest_framework import viewsets


class MerchantProfileViewSet(viewsets.ModelViewSet):
    serializer_class=MerchantProfileSerializer
    queryset=serializer_class.Meta.model.objects.all()
