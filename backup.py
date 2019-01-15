from pytube import Playlist

main = Playlist("https://www.youtube.com/playlist?list=UUlfutpRoY0WTVnq0oB0E0wQ", suppress_exception = True)
transparency = Playlist("https://www.youtube.com/playlist?list=UUdqmP4axeI1hNmX20aZsOwg", suppress_exception = True)

main.download_all("backup/Main Channel", skip_existing = True, prefix_number = False)
transparency.download_all("backup/Transparency Channel", skip_existing = True, prefix_number = False)