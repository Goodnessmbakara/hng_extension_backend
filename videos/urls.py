from django.urls import path
from . import views

urlpatterns = [
    path('start_recording/', views.start_recording, name='start_recording'),
    path('append_video/<int:video_id>/', views.AppendVideoView.as_view(), name='append_video'),
    path('stop_recording/<int:video_id>/', views.StopRecordingView.as_view(), name='stop_recording'),
    path('get_video/<int:video_id>/', views.RetrieveVideoView.as_view(), name='get_video'),
]
