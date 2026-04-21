import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}
date=input("Which year do you want to travel to? Type the data in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENTID=os.getenv("CLIENTID")
CLIENTSECRET=os.getenv("CLIENTSECRET")

response = requests.get(url, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

titles_list=soup.select("li ul li h3")
year=date.split("-")[0]
title_list=[title.get_text().strip() for title in titles_list]

print(title_list)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                               client_secret=CLIENTSECRET,
                                               redirect_uri="http://127.0.0.1:8080",
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]
print(f"Successfully logged in as: {user_id}")
uri_list=[]
try:
    for x in title_list:
        result=sp.search(q=f"track:{x} year:{year}", type="track", limit=1)
        uri_list.append(result["tracks"]["items"][0]["uri"])
except Exception as e:
    print(f"{x} dosent exist un spotify hence skipped")

name=f"{date} BillBoard top 100"
# playlist=sp.current_user_playlist_create(name, public=False, collaborative=False, description=f"{year} BillBoard top 100")
PLAYLIST_ID=os.getenv("PLAYLIST_ID")
sp.playlist_add_items(PLAYLIST_ID,uri_list, position=None)

