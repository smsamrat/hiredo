from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('category', CategoryView),
router.register('question', QuestionsView),
router.register('answer', AnswerView),
router.register('JobPostCreate', JobPostCreate,basename='JobPostCreate'),
router.register('PostLocation', PostLocation,basename='PostLocation'),
router.register('WishlistCompanyViewSet', WishlistCompanyViewSet,basename='WishlistCompanyViewSet'),
router.register('WishlistFeatureViewSet', WishlistFeatureViewSet,basename='WishlistFeatureViewSet'),
router.register('RealTimeBookNowServiceCreate', RealTimeBookNowServiceCreate,basename='RealTimeBookNowServiceCreate'),

urlpatterns = [
    path('', include(router.urls)),
    path('jobpostlistview/', JobPostListView.as_view()),
    path('JobPostListDetail/<int:id>/', JobPostListDetail.as_view()),
    path('JobPostListDelete/<int:id>/', JobPostListDelete.as_view()),
    path('JobPostPerUserView/', JobPostPerUserView.as_view(),name="JobPostPerUserView"),
    path('SendEmailTemplate/', SendEmailTemplate.as_view(),name="SendEmailTemplate"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('RealTimeService/', RealTimeService.as_view(),name="RealTimeService"),
    path('PendingPost/', PendingPost.as_view(),name="PendingPost"),
    path('SellerPendingRealTimePost/', SellerPendingRealTimePost.as_view(),name="SellerPendingRealTimePost"),
    path('FeatureService/', FeatureService.as_view(),name="FeatureService"),
    path('CreditReduceTransactionView/', CreditReduceTransactionView.as_view(),name="CreditReduceTransactionView"),

    #added by swesadiqul
    path('contact-with-buyer/<int:pk>/', ContactListView.as_view(), name='contact_with_buyer'),
    path('post-request-detail/<int:id>/', PostRequestListDetail.as_view(), name='post_request_detail'),
    path('request-accept-reject/', AcceptRejectListView.as_view(), name='request_accept_reject'),
    path('complete-post-list/', CompletePostListView.as_view(), name='complete_post_list'),
    path('my-reponse-count/', MyResponseCountView.as_view(), name='my_response_count'),
    path('my-reponse/', MyResponseListView.as_view(), name='my_response'),
    path('pending-my-reponse-count/', PendingMyResponseCount.as_view(), name='pending_my_reponse_count'),
    path('my-response/search/', MyResponseSearchView.as_view(), name="my_response_search"),
    path('not-interested/<int:pk>/', NotInterestedView.as_view(), name='not-interested'),
    path('book-now-accept-reject/', BookNowAcceptRejectView.as_view(), name='boo_know_accept_reject'),
    path('seller-completed-post/', SellerCompletedRealTimePostView.as_view(), name='seller_completed_post'),
    path('buyer-completed-post/', BuyerCompletedRealTimePostView.as_view(), name='buyer_completed_post'),
]



