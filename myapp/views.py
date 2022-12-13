from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,UserDataSerializer,PostSerializer
from .models import *

class VoucherViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
    def update(self, request, *args, **kwargs):
        request.data.update({'voucherrows': json.loads(request.data.pop('voucherrows', None))})
        return super().update(request, *args, **kwargs)

class UserDataViewSet(viewsets.ModelViewSet):
    serializer_class = UserDataSerializer
    queryset = serializer_class.Meta.model.objects.filter(user_data__is_merchant=True)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset=serializer_class.Meta.model.objects.all()
    
    