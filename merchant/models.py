from django.db import models

from django.contrib.auth.models import User

class MerchantProfile(models.Model):
    account=models.OneToOneField(User, on_delete=models.CASCADE)
    business_country=models.CharField(max_length=255)
    business_state=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    business_structure=models.CharField(max_length=255)
    industry_classification=models.CharField(max_length=255)
    business_name=models.CharField(max_length=255)
    dba=models.CharField(max_length=255)
    business_address_1=models.CharField(max_length=255)
    business_address_2=models.CharField(max_length=255)
    business_address_state=models.CharField(max_length=255)
    business_address_city=models.CharField(max_length=255)
    business_zip_code=models.CharField(max_length=255)
    years_in_business=models.CharField(max_length=255)
    business_retail=models.BooleanField(default=False)
    business_ecomerce=models.BooleanField(default=False)
    monthly_trans_info=models.CharField(max_length=255)
    price_range=models.CharField(max_length=255)
    avr_trans_amount=models.CharField(max_length=255)
    high_trans_amount=models.CharField(max_length=255)
    low_trans_amount=models.CharField(max_length=255)
    legal_first_name=models.CharField(max_length=255)
    legal_last_name=models.CharField(max_length=255)
    dob=models.DateField(auto_now_add=True)
    legal_rep_email=models.EmailField(max_length=255)
    legal_rep_address=models.CharField(max_length=255)
    legal_rep_address_2=models.CharField(max_length=255)
    legal_rep_state=models.CharField(max_length=255)
    legal_rep_zip=models.CharField(max_length=255)
    mobile_no=models.CharField(max_length=255)
    security_question=models.CharField(max_length=255)
    security_answer=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    otp=models.CharField(max_length=6,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.account.username
    