# Install the moviepy library first with: pip install moviepy
import moviepy.editor

# Give the file location as a parameter
video = moviepy.editor.VideoFileClip('video.mp4')

audio_video = video.audio

# Give a location to save the file, as a parameter
audio_video.write_audiofile('audio.mp3')
