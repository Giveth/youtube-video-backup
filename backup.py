from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=UUdqmP4axeI1hNmX20aZsOwg")

playlist.download_all("backup", skip_existing = True)