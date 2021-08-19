from yt_libraries import *

link = 'https://www.youtube.com/watch?v=rc_y0H4Rb2I'

class Video:
    def __init__(self, code, title):
        self.code = code
        self.title = title
# working
    def download_subtitles(self):
        srt = YouTubeTranscriptApi.get_transcript(self.code, languages=["pl"])
        with open(f"{self.title}.txt", "w") as f:
            for i in srt:
                f.write(f"{i}\n")

test1 = Video("rc_y0H4Rb2I", "Kierowca taksówki był GŁUCHY! 😮 Billie Sparrow")
test1.download_subtitles()