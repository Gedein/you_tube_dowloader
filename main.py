from pytube import YouTube


def on_dowload_progress(stream,chunk,bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download*100 / stream.filesize
    print ("Progression de telechargement",int(percent),"%")


Base_url_youtube = "https://www.youtube.com/"

while True:
    url = input("Entrer l'url à télécharger : ").lower()
    if url[:len(Base_url_youtube)] == Base_url_youtube:
        break
    print ("ERREUR VOUS DEVEZ ENTRER UNE URL COMMENCANT PAR ", Base_url_youtube)

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_dowload_progress)

print("TITRE : "+ str(youtube_video.title))
print("NB VUES : " + str(youtube_video.views))

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(""+ str (stream))

# stream = youtube_video.streams.get_by_itag(22)
stream = youtube_video.streams.get_highest_resolution()
print("telechargement....")
print("OK")
stream.download()