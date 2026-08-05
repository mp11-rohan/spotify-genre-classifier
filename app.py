import streamlit as st
from src import pipeline as pipe
from src import spotify_client as spc
import customtkinter as tk

playists = {playlist['name']:playlist['id'] for playlist in spc.user_own_playlists()}
playists["Liked Songs"] = "LIKED_SONGS"
# st.selectbox(label="Choose a playlist:", options=playists.keys())
