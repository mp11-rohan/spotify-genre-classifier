from auth import sp as sp

# Get all playlists of user
def get_user_playlists():
    items = [] # Empty list of playlists
    data = sp.current_user_playlists()
    while data['next'] != None:
        items.extend(data['items'])
        data = sp.next(data)

    items.extend(data['items']) # Last page of data
    return items

# Return playlist which user owns
def user_own_playlists():
    usr_id = sp.current_user()['id']
    return [playlist for playlist in get_user_playlists() if (playlist['collaborative'] == True or usr_id == playlist['owner']['id'])]

# Get Liked Songs of user
def get_user_liked_songs():
    items = []
    data = sp.current_user_saved_tracks(limit=50)
    while data['next'] != None:
        items.extend(data['items'])
        data = sp.next(data)

    items.extend(data['items'])
    return items

# Get the tracks of a specific playlist
def get_tracks_from_playlist(playlist_id):
    tracks = []
    data = sp.playlist_items(playlist_id=playlist_id, limit=100)
    while data['next'] != None:
        tracks.extend(data['items'])
        data = sp.next(data)

    tracks.extend(data['items'])
    return tracks

# Create destination playlist with given name
def create_destination_playlist(playlist_name):
    playlist_info = sp.current_user_playlist_create(name=playlist_name)
    return playlist_info['id']

# Add tracks to playlist through URI
def add_tracks_to_playlist(playlist_id, tracks_list):
    for i in range(0, len(tracks_list), 100):
        chunk = tracks_list[i:i+100]
        sp.playlist_add_items(playlist_id=playlist_id, items=chunk)

# Get song names of given playlist (purpose: genre building)
# songs = [track['item']['name'] for track in get_tracks_from_playlist("3ZRMgkmavJsv6EM9AYDBF3")]
# print(songs)
# print(len(songs))
