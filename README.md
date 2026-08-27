# Spotify Genre Classifier

A desktop app that scans your Spotify playlists and sorts tracks into a destination playlist by genre, based on their audio characteristics.

## What It Does

1. Log in with your Spotify account.
2. Pick a **source** — your Liked Songs or any playlist you own or collaborate on.
3. Pick a **destination** — an existing or new playlist.
4. Pick a **mood** from a predefined list.
5. Click **Classify Playlist** — the app fetches your source tracks, pulls their audio features, scores each one against the genre's thresholds, and adds the ones that qualify to your destination playlist.

You'll see how many tracks were added, plus a button to open the resulting playlist in your browser.

## Features

- Spotify OAuth login — secure, no credentials stored in the app.
- Source: Liked Songs or any owned/collaborative playlist.
- Destination: existing or new playlist, picked from a dropdown.
- Genre-based scoring using audio features (danceability, energy, acousticness, etc.) via ReccoBeats API.
- Local caching of audio features — avoids re-fetching the same tracks on repeat runs.

## Why ReccoBeats?

Spotify deprecated its own `audio-features` and `audio-analysis` endpoints for all new registered developer apps in November 2024.

At first this seemed a total blocker and I was about to give up, but after doing some late night research, many forums mentioned a service that claimed to offer the exact endpoints that Spotify had depracated. This service is **ReccoBeats**, a third-party service, that supplies the audio features (danceability, energy, acousticness, and more) that power the genre scoring.

## Requirements

- **Python 3.14**.
- **spotipy** — Spotify Web API client (OAuth, playlist reads/writes).
- **ReccoBeats API** — audio feature data.
- **CustomTkinter**.
- **pandas / numpy** — data analysis during genre threshold tuning.
- **python-dotenv**.
- **PyInstaller**.


## Setup

### For most users
1. Go to the [Releases](<yet to build>) page and download the latest `SpotifyGenreClassifier.exe`.
2. Double-click to run it.
3. A browser window will open — log in with your Spotify account and grant access.
4. That's it — the app is ready to use.

### For developers (running from source)
1. Clone the repo:
```bash
   git clone https://github.com/mp11-rohan/spotify-genre-classifier.git
   cd spotify-genre-classifier
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Register your own Spotify Developer app at [developer.spotify.com](https://developer.spotify.com/dashboard), and set the redirect URI to: http://127.0.0.1:8888/callback.

5. Create a `.env` file in the project root:
   SPOTIFY_CLIENT_ID = your_client_id
   SPOTIFY_CLIENT_SECRET = your_client_secret
   SPOTIFY_REDIRECT_URI = http://127.0.0.1:8888/callback.

6. Run the app:
```bash
   python app.py
```

## Known Limitations

- **ReccoBeats coverage gaps** — not every track has audio features data available, some tracks are silently skipped (the app reports how many were excluded).
- **Genre thresholds are a first pass** — currently hand-tuned; expect imperfect classification on edge-case tracks.
- **Only one genre is fully built** (Hip Hop & Rap) — more genres are planned.
