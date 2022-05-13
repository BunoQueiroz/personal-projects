from strong_pw_generator import Lists
from youtube_download import YoutubeDownload

teste = Lists()
teste1 = teste.generator_password()
print(f"Sua senha é: {teste1}")

#-------------------------------------------------------------------------------------------------------------------------------------------------

url = "https://www.youtube.com/watch?v=t_-vikOGe8c"
teste2 = YoutubeDownload(url)
teste2.download_mp4()