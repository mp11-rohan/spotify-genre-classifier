import requests

# Fetch features by track_id
def fetch_tracks_features(list_tracks_id):
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
    track_features = []
    for i in range(0, len(list_tracks_id), 40):
        batch = list_tracks_id[i:i+40]
        response = fetch_tracks_features(batch)
        track_features.extend(response['content'])

    return track_features




