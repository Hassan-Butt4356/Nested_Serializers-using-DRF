# Generated by Django 4.1.3 on 2022-12-09 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_country', models.CharField(max_length=255)),
                ('business_state', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('business_structure', models.CharField(max_length=255)),
                ('industry_classification', models.CharField(max_length=255)),
                ('business_name', models.CharField(max_length=255)),
                ('dba', models.CharField(max_length=255)),
                ('business_address_1', models.CharField(max_length=255)),
                ('business_address_2', models.CharField(max_length=255)),
                ('business_address_state', models.CharField(max_length=255)),
                ('business_address_city', models.CharField(max_length=255)),
                ('business_zip_code', models.CharField(max_length=255)),
                ('years_in_business', models.CharField(max_length=255)),
                ('business_retail', models.BooleanField(default=False)),
                ('business_ecomerce', models.BooleanField(default=False)),
                ('monthly_trans_info', models.CharField(max_length=255)),
                ('price_range', models.CharField(max_length=255)),
                ('avr_trans_amount', models.CharField(max_length=255)),
                ('high_trans_amount', models.CharField(max_length=255)),
                ('low_trans_amount', models.CharField(max_length=255)),
                ('legal_first_name', models.CharField(max_length=255)),
                ('legal_last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('legal_rep_email', models.EmailField(max_length=255)),
                ('legal_rep_address', models.CharField(max_length=255)),
                ('legal_rep_address_2', models.CharField(max_length=255)),
                ('legal_rep_state', models.CharField(max_length=255)),
                ('legal_rep_zip', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=255)),
                ('security_question', models.CharField(max_length=255)),
                ('security_answer', models.CharField(max_length=255)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
