from src import spotify_client as spc
from src import reccobeats_client as rcc
from src import genres as gr
from src import scoring as sc

def run_pipeline(origin_playlist_id = None, destination_playlist_id = None, new_playlist_name = None, selected_genre = None):

    # Get tracks from chosen origin playlist
    if origin_playlist_id == "LIKED_SONGS":
        origin_tracks = [track['track']['id'] for track in spc.get_user_liked_songs()]
    else:
        origin_tracks = [track['item']['id'] for track in spc.get_tracks_from_playlist(origin_playlist_id)]

    # Get tracks from chose destination playlist
    if destination_playlist_id == None:
        dest_tracks = set()
    else:
        dest_tracks = set([track['item']['id'] for track in spc.get_tracks_from_playlist(destination_playlist_id)])

    # Eliminate tracks that are already present in destination
    new_tracks = [track for track in origin_tracks if track not in dest_tracks]
    new_tracks = list(set(new_tracks))
    
    # Get feats for new songs
    track_feats = rcc.get_feats_with_cache(new_tracks)

    # Select passed songs for chosen genre
    passed_tracks = [track_feat for track_feat in track_feats['features'] if sc.pass_track(track_feat, selected_genre)]

    # Check if passed_tracks > 0
    if len(passed_tracks) <= 0:
        return {"playlist_url": None, "added_count": 0}

    # Add songs to dest_playlist, create it if needed
    if destination_playlist_id == None:
        destination_playlist_id = spc.create_destination_playlist(new_playlist_name)
    passed_tracks_ids = [rcc.get_id_from_feat(track_feat=track_feat) for track_feat in passed_tracks]
    passed_tracks_uris = [f"spotify:track:{id}" for id in passed_tracks_ids]
    spc.add_tracks_to_playlist(destination_playlist_id, passed_tracks_uris)

    # Return playlist link + count of added tracks
    playlist_uri = f"https://open.spotify.com/playlist/{destination_playlist_id}"
    return {"playlist_url": playlist_uri, "added_count": len(passed_tracks)}