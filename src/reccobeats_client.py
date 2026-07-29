import requests
import os
import json
import config

# Fetch features by track_id
def fetch_tracks_feats(list_tracks_id):
    url = "https://api.reccobeats.com/v1/audio-features"
    headers = {
    'Accept': 'application/json'
    }
    params = {
        'ids' : ','.join(list_tracks_id)
    }

    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

# Slice list to 40 items and get features from batch calls
def chunk_list(list_tracks_id):
    track_feats = []
    for i in range(0, len(list_tracks_id), 40):
        batch = list_tracks_id[i:i+40]
        response = fetch_tracks_feats(batch)
        track_feats.extend(response['content'])

    return track_feats

# Get Spotify ID from 'href' key in the dict
def get_id_from_feat(track_feat):
    href = track_feat['href'].split('/')
    return href[-1]

def get_cached_feats():
    if os.path.exists(config.CACHE_PATH):
        with open(config.CACHE_PATH, "r") as f:
            return json.load(f)
    else:
        return {}

def save_cached_feats(data):
    with open(config.CACHE_PATH, "w") as f:
        json.dump(data, f)

def get_feats_with_cache(track_ids):
    cache = get_cached_feats()

    # Split list between cached tracks and not
    cached_ids = [track for track in track_ids if track in cache]
    missing_ids = [track for track in track_ids if track not in cache]

    # Fetch missing features
    missing_feats = chunk_list(missing_ids)

    # Add missing features to cache keyed with ID
    for feat in missing_feats:
        feat_id = get_id_from_feat(feat)
        cache[feat_id] = feat

    # Save cache to disk
    save_cached_feats(cache)

    found = [cache[track_id] for track_id in track_ids if track_id in cache]
    missing = [track_id for track_id in track_ids if track_id not in cache]

    return {"features": found, "missing": missing}
