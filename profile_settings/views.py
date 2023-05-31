from profile_settings.models import *
from profile_settings.serializers import *
from rest_framework import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
#permission
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser
from django.contrib.auth import get_user_model
User = get_user_model()

# About
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def about_list(request):

    if request.method == 'GET':

        snippets = About.objects.filter(user=request.user)
        serializer = AboutSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AboutSerializer(data=request.data)
        print(request.data.get('user'))
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def about_detail(request, pk):

    try:
        snippet = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AboutSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AboutSerializer(snippet, data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Photos
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def photo_list(request):

    if request.method == 'GET':
        snippets = Photo.objects.filter(user=request.user)
        serializer = PhotoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.user)
        serializer = PhotoSerializer(data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def photo_detail(request, pk):

    try:
        snippet = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhotoSerializer(snippet, data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# bagde

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def badge_list(request):

    if request.method == 'GET':

        snippets = Badge.objects.filter(user=request.user)
        serializer = BadgeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BadgeSerializer(data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def badge_detail(request, pk):

    try:
        snippet = Badge.objects.get(pk=pk)
    except Badge.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BadgeSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BadgeSerializer(snippet, data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Social_Media_Link
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def social_list(request):

    if request.method == 'GET':

        snippets = Social_Media_Link.objects.filter(user=request.user)
        serializer = SocialMediaLinkSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialMediaLinkSerializer(data=request.data)
        request.data['user'] =  request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def social_detail(request, pk):

    try:
        snippet = Social_Media_Link.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialMediaLinkSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialMediaLinkSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Account_Details
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Account_Details_list(request):

    if request.method == 'GET':

        snippets = Account_Details.objects.filter(user=request.user)
        serializer = Account_DetailsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Account_DetailsSerializer(data=request.data)
        request.data['user'] =  request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def account_details_detail(request, pk):

    try:
        snippet = Account_Details.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Account_DetailsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Account_DetailsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserFilter(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk=None,format=None):
        if pk:
            user_single = self.get_object(pk)
            avg_rating = ReviewRating.objects.filter(reviewed_user=pk).aggregate(Avg('rating'))['rating__avg']
            # print(avg_rating)
            serializer =  UserSerializer(user_single)
            # print(serializer.data)
            data = {
                'result':serializer.data,
                'avg_rating':avg_rating,
            }
            return Response(data)
        else:
            user =User.objects.all()
            serializer =  UserSerializer(user,many=True)
            return Response(serializer.data)

# Review & Ratting
class CreateReview(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return ReviewRating.objects.get(pk=pk)
        except ReviewRating.DoesNotExist:
            raise Http404

    def get(self,request,pk=None,format=None):
        if pk:
            review = self.get_object(pk=pk)
            serializer = ReviewRatingSerializer(review).data
            return Response(serializer)
        else:
            review = ReviewRating.objects.filter(reviewed_user = request.user)
            serializer = ReviewRatingSerializer(review,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ReviewRatingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(reviewed_by=request.user)
            return Response({'status':'Review successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk, format=None):
        single_review = self.get_object(pk)
        serializer = ReviewRatingSerializer(single_review, data = request.data)
        if serializer.is_valid():
            serializer.save(reviewed_by=request.user)
            return Response({'status':'Review update successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({'status':'Review Delete successful'},status=status.HTTP_204_NO_CONTENT)



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser] # include MultiPartParser for file uploads

    def get(self, request):
        # Get the Profile object for the current user
        try:
            profile = request.user.user_profile
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        # Calculate percentage complete
        total_fields = 8  # Total number of fields in the Profile model
        filled_fields = sum(bool(getattr(profile, field)) for field in ['image', 'credit', 'badges'])
        filled_fields += sum(bool(getattr(request.user, field)) for field in ['full_name', 'date_of_birth', 'corporation_name', 'corporation_number', 'phone_number'])
        percentage_complete = round(filled_fields / total_fields * 100)

        # Update percentage complete counter for each filled field
        if profile.image:
            profile.image_percentage_complete = 1
        if profile.credit is not None:
            profile.credit_percentage_complete = 1
        if profile.badges.exists():
            profile.badges_percentage_complete = 1
        if request.user.full_name:
            profile.full_name_percentage_complete = 1
        if request.user.date_of_birth:
            profile.date_of_birth_percentage_complete = 1
        if request.user.corporation_name:
            profile.corporation_name_percentage_complete = 1
        if request.user.corporation_number:
            profile.corporation_number_percentage_complete = 1
        if request.user.phone_number:
            profile.phone_number_percentage_complete = 1
        profile.save()

        # Serialize the Profile object and return it in the response, including percentage complete
        serializer = ProfileSerializer(profile)
        data = serializer.data
        data['percentage_complete'] = percentage_complete
        return Response(data)

    def put(self, request):
        # Get the Profile object for the current user
        try:
            profile = request.user.user_profile
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the request data and update the Profile object
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Update percentage complete counter for each filled field
            if 'image' in request.data:
                profile.image_percentage_complete = 1
            if 'credit' in request.data:
                profile.credit_percentage_complete = 1
            if 'badges' in request.data:
                profile.badges_percentage_complete = 1
            if 'full_name' in request.data:
                profile.full_name_percentage_complete = 1
            if 'date_of_birth' in request.data:
                profile.date_of_birth_percentage_complete = 1
            if 'corporation_name' in request.data:
                profile.corporation_name_percentage_complete = 1
            if 'corporation_number' in request.data:
                profile.corporation_number_percentage_complete = 1
            if 'phone_number' in request.data:
                profile.phone_number_percentage_complete = 1
            profile.save()

            return Response({'message': 'Profile update successful.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ChangeUserType(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        is_user = request.data.get('is_user', user.is_user)
        is_professional = request.data.get('is_professional', user.is_professional)

        # Update user type fields
        if is_user and not is_professional:
            user.is_user = False
            user.is_professional = True
        elif is_professional and not is_user:
            user.is_user = True
            user.is_professional = False
        else:
            user.is_user = is_user
            user.is_professional = is_professional

        user.save()

        # Return success response
        return Response({'message': 'User type updated successfully'}, status=status.HTTP_200_OK)


class HelpTopicListView(APIView):
    # permission_classes = [IsAdminUser]


    def get(self, request, *args, **kwargs):
        queryset = HelpTopic.objects.all()
        serializer = HelpTopicSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data
        title = data.get('title')

        # Check if a HelpTopic with the same title already exists
        try:
            help_topic = HelpTopic.objects.get(title=title)
            return Response({'message': 'Help topic already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except HelpTopic.DoesNotExist:
            pass

        serializer = HelpTopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully added help topic.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)


class HelpTopicDetailView(APIView):
    def get_object(self, id):
        try:
            return HelpTopic.objects.get(id=id)
        except HelpTopic.DoesNotExist:
            raise Http404


    def get(self, request, id, format=None):
        topic = self.get_object(id)
        serializer = HelpTopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id=None, format=None):
        topic = self.get_object(id)
        serializer = HelpTopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully help topic updated.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None, format=None):
        topic = HelpTopic.objects.filter(id=id)
        topic.delete()
        return Response({'message': 'Successfully delete help topic.'}, status=status.HTTP_204_NO_CONTENT)


class HelpListView(APIView):
    def get(self, request):
        topics = HelpTopic.objects.all()
        data = []

        for topic in topics:
            helps = Help.objects.filter(topic=topic)
            help_data = []

            for help in helps:
                help_data.append({
                    'id': help.id,
                    'question': help.question,
                    'answer': help.answer
                })

            data.append({
                'id': topic.id,
                'title': topic.title,
                'helps': help_data
            })

        return Response(data)


    def post(self, request, *args, **kwargs):
        data = request.data
        topic = data.get('topic')
        question = data.get('question')

        if Help.objects.filter(topic=topic, question=question).exists():
            return Response({'message': 'Help data already exists.'}, status=status.HTTP_409_CONFLICT)

        serializer = HelpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully added help data.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)


class HelpDetailView(APIView):
    def get_object(self, id):
        try:
            return Help.objects.get(id=id)
        except Help.DoesNotExist:
            raise Http404


    def get(self, request, id, format=None):
        help = self.get_object(id)
        serializer = HelpSerializer(help)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id=None, format=None):
        help = self.get_object(id)
        serializer = HelpSerializer(help, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully help data updated.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None, format=None):
        help = Help.objects.filter(id=id)
        help.delete()
        return Response({'message': 'Successfully delete help data.'}, status=status.HTTP_204_NO_CONTENT)


class StillNeedHelpListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = StillNeedHelp.objects.all()
        serializer = StillNeedHelpSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StillNeedHelpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Thanks for contact with us.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)



class ProfilePictureUpdateView(APIView):
    def patch(self, request, pk):
        try:
            instance = Profile.objects.get(pk=pk)
            image = request.data.get('image')

            if image:
                instance.image = image
                instance.save()

                return Response({'message': 'Image field updated successfully.'})
            else:
                return Response({'message': 'Image field is required.'}, status=400)

        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found.'}, status=404)





