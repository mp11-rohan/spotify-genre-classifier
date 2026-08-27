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
