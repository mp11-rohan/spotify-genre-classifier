from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import config

scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
# sp = user
sp = Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, redirect_uri=config.REDIRECT_URI, scope=scope))

