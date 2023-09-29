from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from .views import  VideoCreateView, VideoListView #ProfileDetailView, ProfileUpdateView,

urlpatterns = [

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    # path('profile/edit/', ProfileUpdateView.as_view(), name='profile-update'),
    path('videos/upload/', VideoCreateView.as_view(), name='video-upload'),
    path('videos/', VideoListView.as_view(), name='video-list'),
]
