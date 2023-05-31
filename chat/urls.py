from django.urls import include, path
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register('category', CategoryView),
# router.register('question', QuestionsView),
# router.register('answer', AnswerView),
# router.register('JobPostCreate', JobPostCreate,basename='JobPostCreate'),
# router.register('PostLocation', PostLocation,basename='PostLocation'),
# router.register('WishlistCompanyViewSet', WishlistCompanyViewSet,basename='WishlistCompanyViewSet'),
# router.register('WishlistFeatureViewSet', WishlistFeatureViewSet,basename='WishlistFeatureViewSet'),
# router.register('RealTimeBookNowServiceCreate', RealTimeBookNowServiceCreate,basename='RealTimeBookNowServiceCreate'),

urlpatterns = [
    # path('', include(router.urls)),
    path('person/<int:id>/', MessageView.as_view()),
    path('inbox/', InboxView.as_view()),

]



