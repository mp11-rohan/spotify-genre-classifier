from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID") or '864fa183e40e43c2ab820c6f46d20819'
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET") or '1c8205f21a5b469e8ac56d251722b259'
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI") or 'http://127.0.0.1:8888/callback'
CACHE_PATH = os.path.join(os.path.dirname(__file__), "..", "tracks_cache.json")