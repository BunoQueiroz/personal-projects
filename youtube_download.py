from pytube import YouTube

class YoutubeDownload:
    def __init__(self, url):
        if self.validation_url(url):
            self.url = url

    def validation_url(self, url):
        if url.find("https://www.youtube.com/watch?v="):
            raise ValueError("URL inválida!")
        else:
            return True

    def verify_resolution(self, resolution):
        if resolution == "360p":
            itag = 18
        elif resolution == "720p":
            itag = 22
        return itag

    def download_mp4(self, resolution="720p"):
        itag = self.verify_resolution(resolution)
        yt = YouTube(self.url)
        filt = yt.streams.filter(file_extension="mp4")
        download = filt.get_by_itag(itag)
        download.download(output_path="D:/Bruno/teste")
        message = "Download concluído com sucesso!!"
        return message