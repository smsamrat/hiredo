from django.shortcuts import render, get_object_or_404
from .models import *
from account.models import *
from .serializers import *
from account.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models import Sum,Avg,Q
from profile_settings.models import Profile, ReviewRating
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404




# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class  = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cat_name__cat']


class QuestionsView(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class  = QuestionsSerializer
    filter_backends = [DjangoFilterBackend]
    # global filterset_fields
    # filterset_fields = ['cat']


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class  = AnswerSerializer


class JobPostCreate(viewsets.ModelViewSet):
    serializer_class  = PostSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        print(self.request.user)
        post_query = Post.objects.all()
        return post_query

    def create(self, request, **kwargs):
        post_data = request.data
        print(post_data)
        print(len(post_data))
        if len(post_data) >= 2:
            post_list = PostList(user = request.user)
            post_list.save()

            credit_list = []

            for data in post_data:
                print(data['question'])
                post = Post.objects.create(
                    post_user = request.user,
                    category_id = data['category'],
                    question_id = data['question'],
                    p_answer_id = data['p_answer'],
                )
                post_list.post_object.add(post)

                credit_number = Answer.objects.get(id=data['p_answer'])
                print(credit_number.credit,"credit")
                credit_list.append(credit_number.credit)
            # print(sum(credit_list),"credit_list")

            post_list.category_id = data['category']
            post_list.location = data['location']
            post_list.latitude = data['latitude']
            post_list.longitude = data['longitude']
            post_list.post_credit = sum(credit_list)
            post_list.save()

            ct = Category.objects.get(id=data['category'])
            print(ct)
            ct.popularity += 1
            ct.save()
        else:
            return Response({'status':'At least add two question from admin for creating a Lead or Post'})

        serializer = PostSerializer(post)
        return Response({'status':'success'})


class PostListFilter(FilterSet):
    min_salary = filters.CharFilter(method="filter_by_min_salary")
    max_salary = filters.CharFilter(method="filter_by_max_salary")

    class Meta:
        model = PostList
        fields = ('category','location',)

    def filter_by_min_salary(self, queryset, name, value):
        queryset = queryset.filter(profile__salary__gt=value)
        return queryset

    def filter_by_max_salary(self, queryset, name, value):
        queryset = queryset.filter(profile__salary__lt=value)
        return queryset


class JobPostListView(ListAPIView):
    queryset = PostList.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category','location',]
    # search_fields  = ['location__name']
    # filterset_class = PostListFilter


class JobPostListDetail(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, id, format=None):
        post_details = PostListSerializer(PostList.objects.get(id=id)).data
        one_click = OneClickResponseSerializer(OneClickResponse.objects.filter(user=request.user),many=True).data
        return Response([post_details, one_click], status=status.HTTP_200_OK)


class JobPostListDelete(APIView):
    def get(self, request, id, format=None):
        post_delete = PostList.objects.get(id=id)
        # print(post_delete.post_object.all(),"Delete")
        if post_delete:
            posts = post_delete.post_object.all()
            for post in posts:
                post.delete()
        post_delete.delete()
        return Response({"message":"delete successfull"}, status=status.HTTP_200_OK)



# class JobPostListView(APIView):
    # def get(self, request, format=None):
    #     query = PostList.objects.all()
    #     serializer = PostListSerializer(query,many=True)
    #     filter_class = Django_filter
    #     search_query = self.request.query_params.get('q','')
    #     print(search_query)
    #     result =[]
    #     if search_query:
    #         for i in serializer.data:
    #             for j in i['post_object']:
    #                 print("category name.....",j['category']['name'])
    #                 if j['category']['name'].startswith(search_query):
    #                     result.append(i)
    #                     break
    #         return Response(result)
    #     else:
    #         return Response(serializer.data)



class JobPostPerUserView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None, format=None):
        print(request.user.id)
        queryset = PostList.objects.filter(user = self.request.user)
        print(queryset)
        serializer = PostListSerializer(queryset,many=True)
        return Response(serializer.data)


class SendEmailTemplate(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        queryset = RecieverEmailTemplate.objects.all()
        serializer = RecieverEmailTemplateSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecieverEmailTemplateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            instance = serializer.save()
            instance.from_user =  request.user
            instance.save()

        return Response(serializer.data)


class PostLocation(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RealTimeService(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = RealTimeServiceserializer
    def get_queryset(self):
        queryset = Service.objects.annotate(total=Avg('user__reviews_received__rating')).order_by('-total')

        if self.request.query_params.get('service_name') and self.request.query_params.get('service_location'):
            queryset = queryset.filter(Q(service_name__name__icontains=self.request.query_params['service_name']), Q(service_location__city__icontains=self.request.query_params['service_location']))
        elif self.request.query_params.get('service_name'):
            queryset = queryset.filter(service_name__name__icontains=self.request.query_params['service_name'])
        elif self.request.query_params.get('service_location'):
            queryset = queryset.filter(Q(service_location__city__icontains=self.request.query_params['service_location']))
        return queryset


class WishlistCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistCompanySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
            return WishlistProfileService.objects.filter(user=self.request.user).annotate(product_rating_avg=Avg('wished_user__reviews_received__rating'))

    def create(self, request, **kwargs):
        data = request.data
        wished_user_object = get_object_or_404(User, id=request.data.get('wished_user'))
        print(wished_user_object,"ggg")
        create_wish = WishlistProfileService.objects.filter(user = request.user,wished_user=wished_user_object)
        if create_wish.exists():
            print(create_wish)
            create_wish.delete()
            serializer = WishlistCompanySerializer(create_wish)
            return Response({'status':'Delete successfull'})
        else:
            create_wish = WishlistProfileService(
                user = request.user,
                wished_user=wished_user_object
            )
            create_wish.save()
            return Response({'status':'successfull'})


class PendingPost(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        return PostList.objects.filter(user = self.request.user,post_type=False)


class FeatureService(ListAPIView):
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    def get_queryset(self):
        queryset = Category.objects.all().order_by('-popularity')
        return queryset


class WishlistFeatureViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistFeatureSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return WishlistFeatureService.objects.filter(user=self.request.user)

    def create(self, request, **kwargs):
        data = request.data
        category_object = get_object_or_404(Category, id=request.data.get('category_service'))
        create_wish = WishlistFeatureService.objects.filter(user = request.user,category_service=category_object)
        if create_wish.exists():
            print(category_object)
            create_wish.delete()
            serializer = WishlistFeatureSerializer(create_wish)
            return Response({'status':'Delete successfull'})
        else:
            create_wish = WishlistFeatureService(
                user = request.user,
                category_service=category_object
            )
            create_wish.save()
            return Response({'status':'successfull'})



#added by swesadiqul
class ContactListView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return PostList.objects.get(pk=pk)
        except PostList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        user = self.request.user

        # check if a response already exists under the po
        if MyResponse.objects.filter(posts=post, user=user).exists():
            return Response({'message': 'You have already responded to this post.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            r_user = Profile.objects.get(user=user)
            avg_rating = ReviewRating.objects.filter(reviewed_user=user).aggregate(Avg('rating'))['rating__avg']
        except ObjectDoesNotExist:
            return Response({'message': 'User profile or review rating not found.'}, status=status.HTTP_400_BAD_REQUEST)

        r_credit = r_user.credit
        serializer = PostListSerializer(post)
        post_credit = serializer.data['post_credit']
        post_id = serializer.data['id']
        if post_credit <= r_credit:
            r_user.credit -= post_credit
            r_user.save()
            post_request_list = PostRequestList(post=post, profile=r_user, rating=avg_rating or 0, request_accepted=False)
            post_request_list.save()
            my_response = MyResponse(user=user, posts=post, status='Pending')
            my_response.save()
            ##added by samrat
            credit_reduce_transaction = CreditReduceTransaction(
                user=request.user,
                lead_post_id = post_id,
                lead_post_credit = post_credit
            )
            credit_reduce_transaction.save()
            return Response({'message': 'Credit has been deducted.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient credit.'}, status=status.HTTP_400_BAD_REQUEST)



class PostRequestListDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, id=None):
        try:
            return PostList.objects.get(id=id, user=request.user)
        except PostList.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        post = self.get_object(request, id)
        queryset = PostRequestList.objects.filter(post=post)
        serializer = PostRequestListSerializer(queryset, many=True)
        return Response(serializer.data)


class AcceptRejectListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = AcceptRejectSerializer(data=request.data)
        if serializer.is_valid():
            postId = serializer.validated_data.get('postId')
            response = serializer.validated_data.get('response')
            userId = serializer.validated_data.get('userId')
            post = PostList.objects.filter(id=postId, user=request.user).first()
            if post is None:
                return Response({'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
            my_response = MyResponse.objects.filter(posts=post, user__id=userId).first()
            if my_response is None:
                return Response({'message': 'Response not found.'}, status=status.HTTP_404_NOT_FOUND)
            post_request_list = PostRequestList.objects.filter(post=post).first()
            if post_request_list is None:
                return Response({'message': 'Post request list not found.'}, status=status.HTTP_404_NOT_FOUND)
            if response == True:
                post.post_type = True
                post.is_response = True
                my_response.status = 'Hired'
                post_request_list.request_accepted = True
                post.save()
                my_response.save()
                post_request_list.save()
                return Response({'message': 'Request accept successfully.'}, status=status.HTTP_200_OK)
            else:
                post.post_type = False
                post.is_response = False
                my_response.status = 'Archived'
                post_request_list.delete()
                # post_request_list.request_accepted = False
                post.save()
                my_response.save()
                # post_request_list.save()
                return Response({'message': 'Request reject successfully.'}, status=status.HTTP_200_OK)

        return Response({'message': 'There was an error processing your request.'}, status=status.HTTP_400_BAD_REQUEST)



class CompletePostListView(APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        post = PostList.objects.filter(user=user, post_type=True).first()
        queryset = PostRequestList.objects.filter(post=post, request_accepted=True)
        serializer = PostRequestListSerializer(queryset, many=True)
        return Response(serializer.data)


class MyResponseCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        queryset = MyResponse.objects.filter(user=user).count()
        data = {
            'my_response_count': queryset,
        }
        return Response(data)


class MyResponseListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        queryset = MyResponse.objects.filter(user=user)

        page = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('page_size', 20)
        paginator = Paginator(queryset, page_size)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        serializer = MyResponseSerializer(paginated_queryset, many=True)
        return Response({'result':serializer.data,'page': paginated_queryset.number,'total_pages': paginator.num_pages,'total_results': paginator.count})


class PendingMyResponseCount(APIView):
    def get(self, request, format=None):
        user = request.user
        try:
            post_responses = MyResponse.objects.filter(user=user, status='Pending')
            pending_count = post_responses.count()
            return Response({'pending_count': pending_count})
        except MyResponse.DoesNotExist:
            raise Http404


from rest_framework import generics, filters
from django.db.models import Q

# class MyResponseSearchView(generics.ListAPIView):
#     serializer_class = MyResponseSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['posts__location', 'posts__category__name', 'status']

#     def get_queryset(self):
#         queryset = MyResponse.objects.filter(user=self.request.user)
#         query = self.request.GET.get('q', None)
#         if query:
#             queryset = queryset.filter(
#                 Q(posts__location__icontains=query) |
#                 Q(posts__category__name__icontains=query) |
#                 Q(status__icontains=query)
#             )
#         return queryset


class MyResponseSearchView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MyResponseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['posts__location', 'posts__category__name', 'status']

    def get_queryset(self):
        queryset = MyResponse.objects.filter(user=self.request.user)
        query = self.request.GET.get('q', None)
        if query:
            queryset = queryset.filter(
                Q(posts__location__icontains=query) |
                Q(posts__category__name__icontains=query) |
                Q(status__icontains=query)
            )
        return queryset

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotInterestedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(PostList, pk=pk)
        post.not_interested_users.add(request.user)
        return Response({'message': 'Post marked as not interested.'}, status=status.HTTP_200_OK)


class RealTimeBookNowServiceCreate(viewsets.ModelViewSet):
    serializer_class  = RealTimeBookNowSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        post_query = RealTimeBookNow.objects.filter(user=self.request.user,post_type=False).annotate(booked_user_avg_rating=(Avg('booked_in_user__reviews_received__rating')))
        # print(post_query)
        return post_query

    def create(self, request, **kwargs):
        post_data = request.data
        print(post_data)
        print(len(post_data))
        # exit()
        if len(post_data) >= 2:
            bookNow_list = RealTimeBookNow(user = request.user)
            bookNow_list.save()

            # credit_list = []

            for data in post_data:
                print(data['question'])
                real_time_book_now = RealTimeBookNowService.objects.create(
                    question_id = data['question'],
                    p_answer_id = data['p_answer'],
                )
                bookNow_list.realtime_post_object.add(real_time_book_now)

                # credit_number = Answer.objects.get(id=data['p_answer'])
                # print(credit_number.credit,"credit")
                # credit_list.append(credit_number.credit)
            # print(sum(credit_list),"credit_list")

            bookNow_list.booked_in_user_id = data['booked_in_user']
            bookNow_list.category_id = data['category']
            bookNow_list.location = data['location']
            bookNow_list.latitude = data['latitude']
            bookNow_list.longitude = data['longitude']
            # bookNow_list.post_credit = sum(credit_list)
            bookNow_list.save()

            # ct = Category.objects.get(id=data['category'])
            # print(ct)
            # ct.popularity += 1
            # ct.save()
        else:
            return Response({'status':'At least add two question from admin for creating a Lead or Post'})

        serializer = RealTimeBookNowServiceSerializer(real_time_book_now)
        return Response({'status':'success'})

    def destroy(self, request, *args, **kwargs):
        real_time_object = self.get_object()
        if real_time_object:
            posts = real_time_object.realtime_post_object.all()
            for post in posts:
                post.delete()
        real_time_object.delete()
        return Response({"status":"delete successfull"}, status=status.HTTP_200_OK)

class SellerPendingRealTimePost(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RealTimeBookNowSerializer
    def get_queryset(self):
        return RealTimeBookNow.objects.filter(booked_in_user = self.request.user,post_type=False)

class CreditReduceTransactionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name')
    user_id = serializers.CharField(source='user.id')
    class Meta:
        model = CreditReduceTransaction
        fields = ['id','user_id','user_name','lead_post_id','lead_post_credit','date']


class BookNowAcceptRejectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = AcceptRejectSerializer(data=request.data)
        if serializer.is_valid():
            postId = serializer.validated_data.get('postId')
            response = serializer.validated_data.get('response')
            userId = serializer.validated_data.get('userId')
            post = RealTimeBookNow.objects.filter(id=postId, booked_in_user__id=userId).first()
            if post is None:
                return Response({'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
            if response == True:
                post.post_type = True
                post.is_response = True
                post.save()
                return Response({'message': 'Request accept successfully.'}, status=status.HTTP_200_OK)
            else:
                post.post_type = False
                post.is_response = False
                post.save()
                return Response({'message': 'Request reject successfully.'}, status=status.HTTP_200_OK)

        return Response({'message': 'There was an error processing your request.'}, status=status.HTTP_400_BAD_REQUEST)


class SellerCompletedRealTimePostView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RealTimeBookNowSerializer
    def get_queryset(self):
        return RealTimeBookNow.objects.filter(booked_in_user = self.request.user, post_type=True)


class CreditReduceTransactionView(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CreditReduceTransactionSerializer
    def get_queryset(self):
        return CreditReduceTransaction.objects.filter(user = self.request.user)

class BuyerCompletedRealTimePostView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RealTimeBookNowSerializer
    def get_queryset(self):
        return RealTimeBookNow.objects.filter(user = self.request.user, post_type=True)




