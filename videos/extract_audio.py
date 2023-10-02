from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_path = video_path.replace(".mp4", ".wav")
    audio_clip.write_audiofile(audio_path)
    return audio_path
