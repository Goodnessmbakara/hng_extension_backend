from rest_framework import generics, status
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer, VideoDetailSerializer
from . import transcribe_video
from rest_framework.decorators import api_view

@api_view(['POST'])
def start_recording(request):
    """
    This view creates a new video object and returns its serialized data.
    """
    video = Video.objects.create()
    serializer = VideoSerializer(video)
    return Response(serializer.data)


class AppendVideoView(generics.UpdateAPIView):
    """
    This class-based view handles updating a video object by appending a new chunk of data.
    """
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_url_kwarg = 'video_id'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().dispatch(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        This method appends a new chunk of data to an existing video.
        If the new chunk is successfully written to the file, it returns a 200 OK status.
        If the new chunk is not provided, it returns a 400 Bad Request status.
        """
        video = self.get_object()

        # Get the new chunk of data from the request
        new_chunk = request.data.get('chunk')

        if new_chunk:
            # Append the new chunk to the existing video data
            with open(video.screen_recording.path, 'ab') as f:
                f.write(new_chunk)

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class StopRecordingView(generics.UpdateAPIView):
    """
    This class-based view handles updating a video object by marking it as finalized.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_url_kwarg = 'video_id'
    
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().dispatch(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
    This class-based view handles retrieving a specific video object.
    """
        video = self.get_object()
        video.finalize = True
        
        video.save()

        # Trigger the transcription task
        #transcribe_video.delay(video.id)

        return Response(status=status.HTTP_200_OK)

class RetrieveVideoView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_url_kwarg = 'video_id'