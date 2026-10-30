from xml.etree.ElementTree import fromstring

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

ClIENT_ID = os.environ["ID"]
CLIENT_SECRET = os.environ["SECRET"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id = ClIENT_ID,
        client_secret = CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date[:4]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
data = response.text
soup = BeautifulSoup(data, "html.parser")

# top_songs = soup.find_all("h3", class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
top_songs = soup.select("li ul li h3")

songs=[]
for song in top_songs:
    songs.append(song.getText(strip=True))

uri_lists = []
for song in songs:
    results = sp.search(
        q=f"track:{song} year:{year}",
        type='track'
    )
    try:
        uri = results["tracks"]["items"][0]["uri"]
        uri_lists.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify")

# pprint(uri_lists)

playlist = sp.current_user_playlist_create(
    name=f"{date} Billboard 100",
    public=False,
    description="Billboard 100",
)

print(playlist)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=uri_lists,
)
