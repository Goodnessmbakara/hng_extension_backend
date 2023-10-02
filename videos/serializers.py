from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.

    Fields:
        id: The video file unique id.
        uploaded_at: The timestamp when the video was first uploaded.
    """
    
    uploaded_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Video
        fields = ('id','uploaded_at')

class VideoDetailSerializer(VideoSerializer):
    screen_recording = serializers.FileField()
    
    class Meta(VideoSerializer.Meta):
        fields = ('id','uploaded_at','screen_recording', 'transcript')