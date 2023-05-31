from django.urls import path
from . views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'slider', SliderViewSet)


#create api endpoint
urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('reset-password-otp/', ResetPasswordOTPAPIView.as_view(), name='reset-password-otp'),
    path('verify-reset-otp/', VerifyOTPAPIView.as_view(), name='verify-reset-otp'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),

    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),

    path('service-location/', ServiceLocationList.as_view(), name='location_list'),
    path('service-location/<int:pk>/', ServiceLocationDetail.as_view(), name='location_detail'),

    path('sms_templates/', SMSTemplateList.as_view(), name='sms_template_list'),
    path('sms_templates/<int:pk>/', SMSTemplateDetail.as_view(), name='sms_template_detail'),

    path('email_templates/', EmailTemplateList.as_view(), name='email_template_list'),
    path('email_templates/<int:pk>/', EmailTemplateDetail.as_view(), name='email_template_detail'),

    path('one-click-responses/', OneClickResponseList.as_view(), name='one_click_response_list'),
    path('one-click-responses/<int:id>/', OneClickResponseList.as_view(), name='one_click_response_update'),
    path('one-click-statuschange/<int:id>/', OneClickStatusChangeView.as_view(), name='one_click_status_change'),

    path('profile_pic_add/', ProfilePictureAdd.as_view(), name='ProfilePictureAdd'),
    path('profile_picture_update/', ProfilePictureUpdate.as_view(), name='ProfilePictureUpdate'),

    path('ServiceWiseLead/', ServiceWiseLead.as_view(), name='ServiceWiseLead'),
    path('ServiceWiseLeadCount/', ServiceWiseLeadCount.as_view(), name='ServiceWiseLeadCount'),

]
urlpatterns += router.urls
