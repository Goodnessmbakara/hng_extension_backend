# # from google.cloud import speech_v1p1beta1 as speech
# from celery import shared_task
# from .models import Video
# from . import extract_audio

# from django.conf import settings

# @shared_task
# def transcribe_video(video_id):
#     video = Video.objects.get(id=video_id)

#     # Here, you would add your code to transcribe the video.
#     audio_url = extract_audio(video.screen_recording) #returns an audio_url
#     audio = speech.RecognitionAudio(uri=audio_url)
#     # This is a placeholder for the actual transcription code.
#     transcript = "This is a placeholder transcript."

#     video.transcript = transcript
#     video.save()

# def transcribe_gcs(audio_path):
#     client = speech.SpeechClient()

#     audio = speech.RecognitionAudio(uri=gcs_uri)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="auto",
#         enable_word_time_offsets=True,
#     )

#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
#         print("Word details:")
#         for word_info in result.alternatives[0].words:
#             word = word_info.word
#             start_time = word_info.start_time
#             end_time = word_info.end_time
#             print(f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}")

# gcs_uri = "gs://bucket_name/path_to_audio_file"
# transcribe_gcs(gcs_uri)
# from google.cloud import speech_v1p1beta1 as speech

# def transcribe_gcs(gcs_uri):
#     client = speech.SpeechClient()

#     audio = speech.RecognitionAudio(uri=gcs_uri)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#         enable_word_time_offsets=True,
#     )

#     response = client.recognize(config=config, audio=audio)

#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
#         print("Word details:")
#         for word_info in result.alternatives[0].words:
#             word = word_info.word
#             start_time = word_info.start_time
#             end_time = word_info.end_time
#             print(f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}")

# gcs_uri = "gs://bucket_name/path_to_audio_file"
# transcribe_gcs(gcs_uri)
