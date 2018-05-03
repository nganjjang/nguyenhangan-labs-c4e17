#PART 1:
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs'

conn = urlopen(url)
raw_top_songs = conn.read()
text = raw_top_songs.decode('utf8')

soup = BeautifulSoup(text, 'html.parser')

section = soup.find('section', 'section chart-grid')

li_list = section.find_all('li')

top_songs_list = []
dl_songs_list =[]
for li in li_list:
    a_name = li.h3.a
    a_artist = li.h4.a
    song_name = a_name.string
    artist = a_artist.string
    top_song = {
        'Song_name' : song_name,
        'Artist' : artist
    }
    top_songs_list.append(top_song)
    dl_song = song_name + ' ' + artist
    dl_songs_list.append(dl_song)

pyexcel.save_as(records=top_songs_list, dest_file_name='Itunes top songs.xlsx')


# PART 2:
from youtube_dl import YoutubeDL
for song in dl_songs_list:
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([song])
