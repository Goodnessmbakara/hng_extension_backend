from rest_framework import generics, permissions
from .models import Video
from .serializers import  VideoSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response


from django.conf import settings
from deepgram import Deepgram



class VideoCreateView(generics.CreateAPIView):
    """
    Create a new video.

    Required permissions: AllowAny

    HTTP Methods:
        - POST: Create a new video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # # Get the uploaded file
        # uploaded_file = request.FILES['screen_recording']

        # # Process the file in chunks
        # for chunk in uploaded_file.chunks():
        #     process(chunk)

        # Transcribe the video using Deepgram
        # dg = Deepgram(settings.DEEPGRAM_API_KEY)
        # transcript = await dg.transcription.prerecorded(serializer.instance.screen_recording.path)

        # # Save the transcript in the database
        # video = serializer.instance
        # video.transcript = transcript.results.channels[0].alternatives[0].transcript
        # video.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class VideoListView(generics.ListAPIView):
    """
    List videos uploaded by the currently authenticated user.

    Required permissions: AllowAny

    HTTP Methods:
        - GET: List videos.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.AllowAny,)
    

# class ProfileDetailView(generics.RetrieveAPIView):
#     """
#     Retrieve the profile of a user.

#     HTTP Methods:
#         - GET: Retrieve the user's profile.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class ProfileUpdateView(generics.UpdateAPIView):
#     """
#     Update the profile of the currently authenticated user.

#     Required permissions: IsAuthenticated, IsOwnerOrReadOnly

#     HTTP Methods:
#         - PUT: Update the user's profile.
#         - PATCH: Partially update the user's profile.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# class SignUpView(APIView):
#     """
#     Register a new user and generate JWT tokens for authentication.

#     HTTP Methods:
#         - POST: Register a new user.
#     """
#     def post(self, request):
#         """
#         Create a new user and generate JWT tokens upon successful registration.

#         Args:
#             request: The request object containing user registration data.

#         Returns:
#             Response: HTTP response containing JWT tokens if registration is successful,
#                       or error messages if there are validation errors.
#         """
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {'refresh': str(refresh), 'access': str(refresh.access_token)},
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
