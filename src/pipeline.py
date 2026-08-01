import spotify_client as sc

def run_pipeline(origin_playlist_id = None, destination_playlist_id = None, new_playlist_name = None, selected_genre = None):

    # Get tracks from chose playlist
    if origin_playlist_id == "LIKED_SONGS":
        origin_tracks = sc.get_user_liked_songs()
    else:
        origin_tracks = sc.get_tracks_from_playlist(origin_playlist_id)

    if destination_playlist_id == None:
        dest_tracks = {}
    else:
        dest_tracks = sc.get_tracks_from_playlist(destination_playlist_id)