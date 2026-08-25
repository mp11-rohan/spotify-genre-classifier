from src import pipeline as pipe
from src import spotify_client as spc
from src import genres as gr
import customtkinter as ctk

# AFTER GUI DONE: playists = {playlist['name']:playlist['id'] for playlist in spc.user_own_playlists()}

app = ctk.CTk()
app.geometry("700x650")
app.title("Spotify Genre Classifier")
app.resizable(False, False)

# Start Title Config
title_frame = ctk.CTkFrame(master=app, width=550, height=50, corner_radius=10, fg_color="#3682A2")
title_frame.pack(pady=20)

title_label = ctk.CTkLabel(
    master=title_frame, 
    text="Spotify Genre Classifier", 
    text_color="#FFFFFF", 
    font=("Cooper Black", 30, "bold")
)
title_label.place(rely=0.5, relx=0.5, anchor="center")
# End Title Config


source_label = ctk.CTkLabel(app, text="Choose source playlist:")
source_label.pack(padx=30, anchor="nw")
# AFTER GUI DONE: source_opts = playists
# AFTER GUI DONE: source_opts["Liked Songs"] = "LIKED_SONGS"
# Set values to list(source_opts.keys()) and add "..." as first option
source_dropdown = ctk.CTkOptionMenu(app, values=["...", "Soft Pop", "Liked Songs"])
source_dropdown.pack(padx=30, pady=15, anchor="nw")

dest_label = ctk.CTkLabel(app, text="Choose destination playlist:")
dest_label.pack(padx=30, anchor="nw")
# AFTER GUI DONE: dest_opts = playists
# dest_opts["Create New"] = None
def on_selection_change(selected_name):
    if selected_name == "Create New":
        new_playlist_entry.pack(padx=30, pady=15, anchor="nw")
    else:
        new_playlist_entry.pack_forget()
dest_dropdown = ctk.CTkOptionMenu(app, values=["...", "Hip-Hop & Rap", "Create New"], command=on_selection_change)
dest_dropdown.pack(padx=30, pady=15, anchor="nw")
new_playlist_entry = ctk.CTkEntry(app, placeholder_text="New playlist name")

gr_label=ctk.CTkLabel(app, text="Choose a mood:")
gr_label.pack(padx=30, anchor="nw", side="top")
gr_opts = list(gr.genres.keys())
gr_opts.insert(0, "...")
gr_dropdown = ctk.CTkOptionMenu(app, values=gr_opts)
gr_dropdown.pack(padx=30, pady=15, anchor="nw", side="top")


app.mainloop()