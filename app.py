from src import pipeline as pipe
from src import spotify_client as spc
from src import genres as gr
import customtkinter as ctk

playists = {playlist['name']:playlist['id'] for playlist in spc.user_own_playlists()}

app = ctk.CTk()
app.geometry("700x650")
app.title("Spotify Genre Classifier")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)


#------------------------------------------Title Config-----------------------------------------------------------------------
title_frame = ctk.CTkFrame(master=app, width=550, height=50, corner_radius=10, fg_color="#3682A2")
title_frame.grid(row=0, column=0, sticky="ew", pady=20, padx=20)

title_label = ctk.CTkLabel(
    master=title_frame, 
    text="Spotify Genre Classifier", 
    text_color="white", 
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

source_opts = {"Liked Songs" : "LIKED_SONGS"}
source_opts.update(playists)
# Set "values" to list(source_opts.keys())
source_dropdown = ctk.CTkComboBox(master=source_frame, values=list(source_opts.keys()), state="readonly")
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

def on_selection_change(selected_name):
    if selected_name == "Create New":
        new_playlist_entry.grid(row=1, column=0,sticky="ew", columnspan=2, padx=10, pady=10)
    else:
        new_playlist_entry.grid_forget()
new_playlist_entry = ctk.CTkEntry(master=dest_frame, placeholder_text="New playlist name")

dest_opts = {"Create New" : None}
dest_opts.update(playists)
dest_dropdown = ctk.CTkComboBox(master=dest_frame, values=list(dest_opts.keys()), command=on_selection_change, state="readonly")
dest_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
#------------------------------------------Genre Config-----------------------------------------------------------------------
gr_frame = ctk.CTkFrame(master=app, width=650, height=60)
gr_frame.grid(row=3, column=0, sticky="ew", pady=20, padx=50)
gr_frame.grid_columnconfigure(1, weight=1)
gr_frame.grid_rowconfigure(0, weight=1)

gr_label=ctk.CTkLabel(
    master=gr_frame,
    text="Choose a mood:",
    text_color="white",
    font=("Arial Rounded MT Bold", 18, "bold")
    )
gr_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
gr_opts = list(gr.genres.keys())
gr_dropdown = ctk.CTkComboBox(master=gr_frame, values=gr_opts, state="readonly")
gr_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

#------------------------------------------Classify Config---------------------------------------
def on_classify():
    source_name = source_dropdown.get()
    source_id = source_opts[source_name]

    dest_name = dest_dropdown.get()
    dest_id = dest_opts[dest_name]

    new_name = new_playlist_entry.get() if dest_name == "Create New" else None

    gr_name = gr_dropdown.get()

    print(f"Source Playlist Name: {source_name}\nSource Playlist ID: {source_id}\nDestination Playlist Name: {dest_name}\nDestination Playlist ID: {dest_id}\nNew Playlist Name: {new_name}\nGenre Selected: {gr_name}")
gen_btn=ctk.CTkButton(
    master=app,
    width=300, 
    height=40, 
    text="Classify Playlist", 
    font=("Arial Rounded MT Bold", 24, "bold"),
    fg_color="#3682A2",
    command=on_classify
    )
gen_btn.grid(row=4, column=0, columnspan=2)


app.mainloop()

""" TO CHANGE:
 - font of labels """