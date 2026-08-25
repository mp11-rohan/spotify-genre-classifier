from src import pipeline as pipe
from src import spotify_client as spc
from src import genres as gr
import customtkinter as ctk

# AFTER GUI DONE: playists = {playlist['name']:playlist['id'] for playlist in spc.user_own_playlists()}

app = ctk.CTk()
app.geometry("700x650")
app.title("Spotify Genre Classifier")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)

#------------------------------------------Title Config-----------------------------------------------------------------------
title_frame = ctk.CTkFrame(master=app, width=550, height=50, corner_radius=10, fg_color="#3682A2")
title_frame.grid(row=0, column=0, sticky="ew", pady=20, padx=20)

title_label = ctk.CTkLabel(
    master=title_frame, 
    text="Spotify Genre Classifier", 
    text_color="#FFFFFF", 
    font=("Cooper Black", 30, "bold")
)
title_label.place(rely=0.5, relx=0.5, anchor="center")

#------------------------------------------Source Config------------------------------------------------------------------------
source_frame = ctk.CTkFrame(master=app, width=650, height=60)
source_frame.grid(row=1, column=0, sticky="ew", pady=20, padx=50)
source_frame.grid_columnconfigure(1, weight=1)
source_frame.grid_rowconfigure(0, weight=1)

source_label = ctk.CTkLabel(
    master=source_frame,
    text="Choose source playlist:",
    text_color="white",
    font=("Arial Rounded MT Bold", 18, "bold")
)
source_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# AFTER GUI DONE: source_opts = playists
# AFTER GUI DONE: source_opts["Liked Songs"] = "LIKED_SONGS"
# Set "values" to list(source_opts.keys())
source_dropdown = ctk.CTkComboBox(master=source_frame, values=["Soft Pop", "Liked Songs"], state="readonly")
source_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

#------------------------------------------Destination Config------------------------------------------------------------------
dest_frame = ctk.CTkFrame(master=app, width=650, height=80)
dest_frame.grid(row=2, column=0, sticky="ew", pady=20, padx=50)
dest_frame.grid_columnconfigure(1, weight=1)
dest_frame.grid_rowconfigure(0, weight=1)

dest_label = ctk.CTkLabel(
    master=dest_frame,
    text="Choose destination playlist:",
    text_color="white",
    font=("Arial Rounded MT Bold", 18, "bold")
)
dest_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
# AFTER GUI DONE: dest_opts = playists
# AFTER GUI DONE: dest_opts["Create New"] = None
def on_selection_change(selected_name):
    if selected_name == "Create New":
        new_playlist_entry.grid(row=1, column=0,sticky="ew", columnspan=2, padx=10, pady=10)
    else:
        new_playlist_entry.grid_forget()
dest_dropdown = ctk.CTkComboBox(master=dest_frame, values=["Hip-Hop & Rap", "Create New"], command=on_selection_change, state="readonly")
dest_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
new_playlist_entry = ctk.CTkEntry(master=dest_frame, placeholder_text="New playlist name")
#------------------------------------------Genre Config-----------------------------------------------------------------------
# gr_label=ctk.CTkLabel(app, text="Choose a mood:")
# gr_label.pack(padx=30, anchor="nw", side="top")
# gr_opts = list(gr.genres.keys())
# gr_dropdown = ctk.CTkComboBox(app, values=gr_opts, state="readonly")
# gr_dropdown.pack(padx=30, pady=15, anchor="nw", side="top")


app.mainloop()

""" TO CHANGE:
 - font of labels """