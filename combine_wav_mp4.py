def test_moviepy(video_path, audio_path, output_path='output-moviepy.mp4', fps=24):
    import moviepy.editor as mpe
    
    print('--- moviepy ---')

    video = mpe.VideoFileClip(video_path)
    video = video.set_audio(mpe.AudioFileClip(audio_path))
    video.write_videofile(output_path, fps=fps)


def test_ffmpeg(video_path, audio_path, output_path='output-ffmpeg.mp4', fps=24):
    import ffmpeg

    print('--- ffmpeg ---')

    video  = ffmpeg.input(video_path).video # get only video channel
    audio  = ffmpeg.input(audio_path).audio # get only audio channel
    output = ffmpeg.output(video, audio, output_path, vcodec='copy', acodec='aac', strict='experimental')
    ffmpeg.run(output)

# --- main ---

video_path  = 'media/masque_of_red_death.mp4'
audio_path  = 'media/27_braids_outro.wav'
output_path = 'output.mp4'

test_moviepy(video_path, audio_path)#, output_path)
test_ffmpeg(video_path, audio_path)#, output_path)