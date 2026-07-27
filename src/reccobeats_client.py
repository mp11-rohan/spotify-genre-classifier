import requests

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






""" 
tracks = ['6o0gJtOgimGamRBTS80H5g', '4vyG9ZhHT8MKJE5mTICMFC', '0eOcjJgpO8XdJbPMYJgKqq', '74nEGIzIefJhJ5qX7NeIAz']
print(fetch_tracks_features(tracks)) """