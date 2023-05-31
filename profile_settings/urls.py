from django.urls import path,include
from profile_settings import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # badge
    path('badge/', views.badge_list),
    path('badge_detail/<int:pk>/', views.badge_detail),

    # about
    path('about/', views.about_list),
    path('about_detail/<int:pk>/', views.about_detail),

    # photo
    path('photo/', views.photo_list),
    path('photo_detail/<int:pk>/', views.photo_detail),

    # social
    path('social/', views.social_list),
    path('social_detail/<int:pk>/', views.social_detail),

    #User
    path('UserFilter/', views.UserFilter.as_view(), name='UserFilter'),
    path('UserFilter/<int:pk>/', views.UserFilter.as_view(), name='UserFilterDetails'),

    #review_list
    path('create_review/', views.CreateReview.as_view(), name='create_review'),
    path('update_review/<pk>/', views.CreateReview.as_view(), name='create_review_details'),

    # Account Details
    path('account_add/', views.Account_Details_list),
    path('account_detail/<int:pk>/', views.account_details_detail),


    #profile related
    path('profile-update/', views.ProfileView.as_view(), name='profile_update'),
    path('change-user-type/', views.ChangeUserType.as_view(), name='change_user_type'),
    path('help-topic/', views.HelpTopicListView.as_view(), name='help_topic'),
    path('help-topic/<int:id>/', views.HelpTopicDetailView.as_view(), name='help_topic_detail'),
    path('help/', views.HelpListView.as_view(), name='help'),
    path('help/<int:id>/', views.HelpDetailView.as_view(), name='help_detail'),
    path('still-need-help/', views.StillNeedHelpListView.as_view(), name='still_need_help'),
    path('profile-picture-update/<int:pk>/', views.ProfilePictureUpdateView.as_view(), name='profile_picture_update'),
]