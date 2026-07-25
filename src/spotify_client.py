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
def get_tracks_from_playlist(list_id):
    tracks = []
    data = sp.playlist_items(playlist_id=list_id, limit=100)
    while data['next'] != None:
        tracks.extend(data['items'])
        data = sp.next(data)

    tracks.extend(data['items'])
    return tracks
