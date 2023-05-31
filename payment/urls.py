from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register('JobPostCreate', JobPostCreate,basename='JobPostCreate'),


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('SetCreditRetrive/', SetCreditRetrive.as_view(),name='SetCreditRetrive'),
    path('UserCreditAmount/', UserCreditAmount.as_view(),name='UserCreditAmount'),
    path('UserCreditPurchased/', UserCreditPurchased.as_view(),name='UserCreditPurchased'),

]