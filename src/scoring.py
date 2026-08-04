import reccobeats_client as rc
import genres as gr
import pandas as pd
import spotify_client as sc

def pass_feature(feat_val, bounds):
    return feat_val >= bounds[0] and feat_val <= bounds[1]

def pass_track(track_feats, genre):
    passed_feats = 0
    for feat in genre['features'].keys():
        if passed_feats >= genre['required']:
            return True
        passed_feats += pass_feature(track_feats[feat], genre['features'][feat])
    return passed_feats >= genre['required']

# songs = rc.get_feats_with_cache([track['item']['id'] for track in sc.get_tracks_from_playlist('5XK6JIbVM0z4smF66Iq330')])
# df_songs = pd.DataFrame(songs['features'])
# df_songs.index = [rc.get_id_from_feat(feat) for feat in songs['features']]
# df_songs['passed'] = df_songs.apply(lambda row: pass_track(row, gr.genres['Hip Hop & Rap']), axis=1)
# pd.set_option('display.max_rows', None)
# print(df_songs[[ 'speechiness', 'instrumentalness', 'danceability', 'acousticness', 'energy', 'passed']])
