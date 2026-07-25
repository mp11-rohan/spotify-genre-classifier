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

"""
TODO: check the last two functions return correct info
      do the last function of level 3
"""