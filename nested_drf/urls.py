from django.contrib import admin
from django.urls import path,include
from myapp.views import (
    VoucherViewSet,
    UserDataViewSet,
    PostViewSet
)
from merchant.views import (
    MerchantProfileViewSet,
)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('voucher', VoucherViewSet,basename='voucher')
router.register('user', UserDataViewSet,basename='user')
router.register('post',PostViewSet,basename='post')

router.register('merchant',MerchantProfileViewSet,basename='merchant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
