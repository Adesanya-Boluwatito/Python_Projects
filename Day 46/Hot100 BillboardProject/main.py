from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "f1a0259b10644509a03657457a8a8caf"
CLIENT_SECRET = "df5a794415324d4987378ef8767d7e9a"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-modify-private",
                                               show_dialog= True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)



date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
Hot_100 = soup.find_all(name="div", class_="o-chart-results-list-row-container")

song_names = []

for res in Hot_100:
    song_name = res.find("h3").getText().strip()
    song_names.append(song_name)


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track{song} year:{year}", type="track")
    print(result)
    # try:
    #     uri = result["tracks"]["items"][0]["uri"]
    #     song_uris.append(uri)
    # except IndexError:
    #     pprint(f"{song} dosen't exist in Spotify. Skipped.")