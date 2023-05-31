from .models import User
from .serializers import *
from account.renderers import UserRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
User = get_user_model()
from rest_framework.parsers import MultiPartParser, FormParser
import pyotp
import datetime
from .otp import *
from rest_framework import viewsets
from django.utils import timezone
from django.db.models import Q
from profile_settings.models import Profile
from profile_settings.serializers import ProfileSerializer
from lead.serializers import *
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404



#create views
def generate_otp():
    # Generate a random secret key
    secret = pyotp.random_base32()

    # Create an OTP object
    totp = pyotp.TOTP(secret, digits=4)

    # Generate the OTP
    otp = totp.now()

    return secret, otp



# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class RegistrationAPIView(APIView):

    def post(self, request):
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists.'}, status=status.HTTP_409_CONFLICT)
        # Create a new User object
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Profile object for the User
        profile = Profile(user=user)
        profile.save()

        one_click_response = OneClickResponse(user=user)
        one_click_response.save()

        # Return a response with the created User and Profile objects
        user_serializer = RegistrationSerializer(user)
        profile_serializer = ProfileSerializer(profile)
        return Response({'message': 'User successfully registered.'}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            data = {'message': 'Email and password are required fields.'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                token = get_tokens_for_user(user)
                serializer = RegistrationSerializer(user)
                access_token = token['access']
                data = {
                    'token': access_token,
                    'message': 'User successfully logged in.',
                    'user': serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {'message': 'Invalid email or password.'}
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            data = {'message': str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out."})


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'status': 'Password changed successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Wrong password.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordOTPAPIView(APIView):
    serializer_class = ResetPasswordOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_or_email = serializer.validated_data['phone_or_email']
        media = serializer.validated_data['media']

        if media == 'email':
            user = User.objects.filter(email=phone_or_email).first()
            if user:
                # Generate and save OTP for the user
                otp_secret, otp = generate_otp()
                user.otp_secret = otp_secret
                user.otp = otp
                user.otp_expire_time = timezone.now() + datetime.timedelta(minutes=4)
                user.save()

                # Send OTP via email
                send_otp_via_email(user.email, otp)

                return Response({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        elif media == 'phone':
            user = User.objects.filter(phone_number=phone_or_email).first()
            if user:
                # Generate and save OTP for the user
                otp_secret, otp = generate_otp()
                user.otp_secret = otp_secret
                user.otp = otp
                user.otp_expire_time = timezone.now() + datetime.timedelta(minutes=4)
                user.save()

                # Send OTP via SMS (using Twilio or other service)
                send_otp_via_sms(user.phone_number, otp)

                return Response({'message': 'OTP has been sent to your phone.'}, status=status.HTTP_200_OK)

        return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


class VerifyOTPAPIView(APIView):
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_or_email = serializer.validated_data['phone_or_email']
        otp = serializer.validated_data['otp']

        user = User.objects.filter(Q(email=phone_or_email) | Q(phone_number=phone_or_email)).first()
        if not user:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if user.otp != otp:
            return Response({'message': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)

        if user.otp_expire_time < timezone.now():
            return Response({'message': 'OTP expired.'}, status=status.HTTP_400_BAD_REQUEST)

        # If OTP is valid and not expired, reset the password
        # Reset the OTP and OTP expire time
        user.otp = None
        user.otp_expire_time = None
        user.save()

        return Response({'message': 'OTP has been verified.'}, status=status.HTTP_200_OK)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_or_email = serializer.validated_data['phone_or_email']
        password = serializer.validated_data['password']

        user = User.objects.filter(Q(email=phone_or_email) | Q(phone_number=phone_or_email)).first()
        if not user:
             return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(password)
        user.save()

        return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)


class ServiceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Service.objects.filter(user=request.user)
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            # Get the service_name id from the request data
            service_name_id = request.data.get('service_name')
            try:
                # Get the service_name object using the provided id
                service_name = Category.objects.get(pk=service_name_id)
            except Category.DoesNotExist:
                return Response({'message': 'This service name does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            # Check if the service with the same name already exists for the user
            if Service.objects.filter(user=request.user, service_name=service_name).exists():
                return Response({'message': 'You have already added this service.'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the service object with the validated data and the retrieved service_name object
            serializer.save(service_name=service_name, user=request.user)
            return Response({"message": "Service created successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Error creating service. Please try again.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Service, pk=pk, user=self.request.user)

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Service updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Service update failed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response({"message": "Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class ServiceLocationList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the user's service locations
        service_locations = ServiceLocation.objects.filter(user=request.user)
        serializer = ServiceLocationSerializer(service_locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Check if the service location already exists
        existing_service_location = ServiceLocation.objects.filter(user=request.user, city=request.data.get('city')).first()
        if existing_service_location:
            return Response({'message': 'Service location already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new service location for the user
        serializer = ServiceLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Service location created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error creating service location', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ServiceLocationDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        # Retrieve the service location based on its primary key and the user
        try:
            service_location = ServiceLocation.objects.get(pk=pk, user=self.request.user)
        except ServiceLocation.DoesNotExist:
            service_location = None
        return service_location

    def get(self, request, pk):
        # Retrieve a specific service location owned by the user
        service_location = self.get_object(pk)
        if service_location is None:
            return Response({'message': f'Service location with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceLocationSerializer(service_location)
        return Response(serializer.data)

    def put(self, request, pk):
        # Update a specific service location owned by the user
        service_location = self.get_object(pk)
        if service_location is None:
            return Response({'message': f'Service location with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceLocationSerializer(service_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Service location updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating service location', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a specific service location owned by the user
        service_location = self.get_object(pk)
        if service_location is None:
            return Response({'message': f'Service location with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)
        service_location.delete()
        return Response({'message': 'Service location deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class SMSTemplateList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        templates = SMSTemplate.objects.filter(user=request.user)
        serializer = SMSTemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SMSTemplateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'SMSTemplate created successfully'}, status=status.HTTP_201_CREATED)
        return Response({"message": "Error creating SMSTemplate. Please try again.", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SMSTemplateDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return SMSTemplate.objects.get(pk=pk, user=self.request.user)
        except SMSTemplate.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        template = self.get_object(pk)
        serializer = SMSTemplateSerializer(template)
        return Response(serializer.data)

    def put(self, request, pk):
        template = self.get_object(pk)
        serializer = SMSTemplateSerializer(template, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SMSTemplate updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid data. Please check the input.'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        template = self.get_object(pk)
        template.delete()
        return Response({'message': 'SMSTemplate deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class EmailTemplateList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        templates = EmailTemplate.objects.filter(user=request.user)
        serializer = EmailTemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmailTemplateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            template_name = serializer.validated_data['template_name']
            existing_template = EmailTemplate.objects.filter(user=request.user, template_name=template_name).first()
            if existing_template:
                return Response({'message': f'Email template "{template_name}" already exists.'}, status=status.HTTP_409_CONFLICT)
            email_template = serializer.save(user=request.user)
            one_click_response = OneClickResponse.objects.filter(user=request.user).first()
            if one_click_response is not None:
                one_click_response.template = email_template
                one_click_response.save()
            else:
                OneClickResponse.objects.create(user=request.user, template=email_template)
            return Response({'message': 'Email template created successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid input. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)


class EmailTemplateDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return EmailTemplate.objects.get(pk=pk)
        except EmailTemplate.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        template = self.get_object(pk)
        serializer = EmailTemplateSerializer(template)
        return Response(serializer.data)

    def put(self, request, pk):
        template = self.get_object(pk)
        serializer = EmailTemplateSerializer(template, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Email Template updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating EmailTemplate. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        template = self.get_object(pk)
        template.delete()
        return Response({'message': 'Email Template deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class OneClickResponseList(APIView):
    def get(self, request, format=None):
        template_id = request.GET.get('template_id')
        queryset = OneClickResponse.objects.filter(user=request.user)
        if template_id:
            queryset = queryset.filter(template_id=template_id)
        serializer = OneClickResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        try:
            one_click_response = OneClickResponse.objects.get(id=id, user=request.user)
        except OneClickResponse.DoesNotExist:
            return Response({'message': 'One-Click Response not found.'}, status=status.HTTP_404_NOT_FOUND)

        template_id = request.data.get('template_id')
        if not template_id:
            return Response({'message': 'Template_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            email_template = EmailTemplate.objects.get(id=template_id, user=request.user)
        except EmailTemplate.DoesNotExist:
            return Response({'message': 'Email Template not found.'}, status=status.HTTP_404_NOT_FOUND)

        one_click_response.template = email_template
        one_click_response.one_click_response = request.data.get('one_click_response', False)
        one_click_response.save()

        serializer = OneClickResponseSerializer(one_click_response)
        return Response(serializer.data)


class OneClickStatusChangeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id, format=None):
        try:
            one_click_response = OneClickResponse.objects.get(id=id, user=request.user)
        except OneClickResponse.DoesNotExist:
            return Response({'message': 'One-Click Response not found.'}, status=status.HTTP_404_NOT_FOUND)

        one_click_response_value = request.data.get('one_click_response')
        if one_click_response_value is not None:
            one_click_response.one_click_response = one_click_response_value

        one_click_response.save()

        serializer = OneClickResponseSerializer(one_click_response)
        return Response(serializer.data)



class ProfilePictureAdd(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = ProfilePictureSerializer(data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Profile Picture Already Exits'}, status=status.HTTP_400_BAD_REQUEST)


class ProfilePictureUpdate(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def put(self, request, format=None):
        serializer = ProfilePictureSerializer(data=request.data)
        if serializer.is_valid():
            user_profile_pic = request.user.user_profile_pic
            user_profile_pic.picture = serializer.validated_data['picture'] ## serializer theke picture field dhora hoise sei field user update profile pic pathaise
            user_profile_pic.save()
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=400)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    parser_classes = (MultiPartParser, FormParser,)
    # permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class ServiceWiseLead(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        qs = Service.objects.filter(user=self.request.user)
        getlist = []
        for i in qs:
            id = i.service_name.id
            getlist.append(id)

        queryset = PostList.objects.filter(category__id__in=getlist).exclude(not_interested_users=request.user)

        if request.GET.get('q'):
            q = PostList.objects.filter(category__name__icontains=request.GET.get('q'))
            serializer = PostListSerializer(q, many=True)
            return Response({'result': serializer.data})
        else:
            page = self.request.query_params.get('page', 1)
            page_size = self.request.query_params.get('page_size', 20)
            paginator = Paginator(queryset, page_size)
            try:
                paginated_queryset = paginator.page(page)
            except PageNotAnInteger:
                paginated_queryset = paginator.page(1)
            except EmptyPage:
                paginated_queryset = paginator.page(paginator.num_pages)

            serializer = PostListSerializer(paginated_queryset, many=True)
            return Response({'result': serializer.data, 'page': paginated_queryset.number, 'total_pages': paginator.num_pages, 'total_results': paginator.count})


class ServiceWiseLeadCount(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        qs = Service.objects.filter(user=self.request.user)
        if len(qs) >= 1:
            getlist = []
            for i in qs:
                id = i.service_name.id
                queryset = PostList.objects.filter(is_response=False,category__id=id)
                if queryset.exists():
                    getlist.append(queryset)
            new_list = [item for sublist in getlist for item in sublist]
            serializer = PostListSerializer(queryset,many=True)
            return Response({'total_lead':len(new_list)})
        else:
            serializer = PostListSerializer(qs,many=True)
            return Response({'total_lead':0})
