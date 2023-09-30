from rest_framework import generics, permissions
from .models import Video
from .serializers import  VideoSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.response import Response


from pydub import AudioSegment
import speech_recognition as sr
import moviepy.editor as mp
import os

import whisper

model = whisper.load_model("base")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("audio.mp3")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)

class VideoCreateView(generics.CreateAPIView):
    """
    Create a new video.

    Required permissions: AllowAny

    HTTP Methods:
        - POST: Create a new video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [FileUploadParser]
    permission_classes = (permissions.AllowAny,)        
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        #Extract audio from the video
        video = mp.VideoFileClip(serializer.instance.screen_recording.path)
        audio_file = video.audio
        audio_file.write_audiofile(f"audio_{serializer.instance.id}.wav")

        # # Transcribe the audio
        r = sr.Recognizer()
        with sr.AudioFile(f"audio_{serializer.instance.id}.wav") as source:
            data = r.record(source)
    
        transcription = r.recognize_google(data)
        print(transcription)
        # # Save the transcription to a file
        # transcription_path = "transcription.txt"
        # with open(transcription_path, "w") as file:
        #     file.write(transcription)

        # # Add the transcription file URL to the response
        # response_data = serializer.data
        # response_data['transcription_file_url'] = request.build_absolute_uri(transcription_path)
        # os.remove(audio_path)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class VideoListView(generics.ListAPIView):
    """
    List videos  currently available on the backend.

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
