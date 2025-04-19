from moviepy.editor import VideoFileClip, AudioFileClip

def combine_audio_video():
    # Load the audio and video files
    audio = AudioFileClip("Vibe_coding_male.mp3")
    video = VideoFileClip("male.mp4")
    
    # Get durations
    audio_duration = audio.duration
    video_duration = video.duration
    
    # Calculate how many times to loop the video
    loop_times = int(audio_duration / video_duration) + 1
    
    # Loop the video to match audio duration
    final_video = video.loop(n=loop_times)
    
    # Set the audio of the final video
    final_video = final_video.set_audio(audio)
    
    # Cut the video to match exact audio duration
    final_video = final_video.subclip(0, audio_duration)
    
    # Write the final video file
    final_video.write_videofile("final_song_female.mp4", codec='libx264', audio_codec='aac')
    
    # Close the clips
    audio.close()
    video.close()
    final_video.close()

if __name__ == "__main__":
    combine_audio_video()