from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MerchantProfile


class UserAccountSerialzier(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=155)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
    
class MerchantProfileSerializer(serializers.ModelSerializer):
    account=UserAccountSerialzier()
    class Meta:
        model=MerchantProfile
        exclude=['otp','dob']

    def create(self,validated_data):
        account=validated_data.pop('account')
        user=User.objects.create(**account)
        print(user)
        merchant=MerchantProfile.objects.create(account=user,**validated_data)
        return merchant
