import yt_dlp
from yt_dlp.utils import download_range_func

def yt_vid_downloader(st, et, name, link, fmt):
    start_time = st[0] * 60 + st[1]
    end_time = et[0] * 60 + et[1] 

    if fmt == 'mp4':
        yt_opts = {
            'verbose': True,
            'download_ranges': download_range_func(None, [(start_time, end_time)]),
            'force_keyframes_at_cuts': True,
            'format': 'best[ext=mp4]',
            'outtmpl': f'C:/Users/nicor/OneDrive/Documents/Code/AudioPipe/media/{name}.{fmt}'
        }

    if fmt == 'wav':
        yt_opts = {
            'verbose': True,
            'download_ranges': download_range_func(None, [(start_time, end_time)]),
            'force_keyframes_at_cuts': True,
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            }],
            'outtmpl': f'C:/Users/nicor/OneDrive/Documents/Code/AudioPipe/media/{name}'
        }


    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download(link)

ST = [18, 36]
ET = [18, 56]
NAME = 'masque_of_red_death'
LINK = 'https://www.youtube.com/watch?v=e9NeA2UR-AY'
FMT = 'mp4'


yt_vid_downloader(ST, ET, NAME, LINK, FMT)    


