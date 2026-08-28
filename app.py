from src import pipeline as pipe
from src import spotify_client as spc
from src import genres as gr
import customtkinter as ctk
import threading
import webbrowser

playlists = {playlist['name']:playlist['id'] for playlist in spc.user_own_playlists()}

#------------------------------------------Functions----------------------------------------------------------------------------------

def on_error(e):
    prog_bar.grid_forget()
    
    gen_btn.configure(state="normal")
    source_dropdown.configure(state="readonly")
    dest_dropdown.configure(state="readonly")
    gr_dropdown.configure(state="readonly")

    result_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
    result_label.configure(text="Something went wrong.")


def run_pipeline_background(source_id, dest_id, new_playlist_name, gr_dict):
    try:
        result = pipe.run_pipeline(
            origin_playlist_id=source_id,
            destination_playlist_id= dest_id,
            new_playlist_name=new_playlist_name,
            selected_genre=gr_dict
        )
        app.after(0, lambda: after_wait(result))
    except Exception as e:
        app.after(0, lambda e=e: on_error(e))

def on_classify():
    source_name = source_dropdown.get()
    dest_name = dest_dropdown.get()
    gr_name = gr_dropdown.get()

    if source_name not in source_opts or dest_name not in dest_opts or gr_name not in gr.genres:
        result_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        result_label.configure(text="Please select a source, destination, and mood.")
        return

    prog_bar.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    result_btn.grid_forget()
    result_label.grid_forget()

    prog_bar.start()

    gen_btn.configure(state="disabled")
    source_dropdown.configure(state="disabled")
    dest_dropdown.configure(state="disabled")
    gr_dropdown.configure(state="disabled")

    source_id = source_opts[source_name]
    dest_id = dest_opts[dest_name]
    new_playlist_name = new_playlist_entry.get() if dest_name == "Create New" else None
    new_playlist_name = f"{gr_name} Playlist" if new_playlist_name == "" and dest_name == "Create New" else new_playlist_name
    gr_dict = gr.genres[gr_name]

    thread = threading.Thread(target=run_pipeline_background, args=(source_id, dest_id, new_playlist_name, gr_dict), daemon=True)
    thread.start()

def on_selection_change(selected_name):
    if selected_name == "Create New":
        new_playlist_entry.grid(row=1, column=0,sticky="ew", columnspan=2, padx=10, pady=10)
    else:
        new_playlist_entry.grid_forget()

def after_wait(result):
    prog_bar.grid_forget()

    gen_btn.configure(state="normal")
    source_dropdown.configure(state="readonly")
    dest_dropdown.configure(state="readonly")
    gr_dropdown.configure(state="readonly")

    if(result['added_count'] == 0):
        result_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        result_label.configure(text=f"No matching songs found.\n{result['missing']} songs were not evaluated.")
    else:
        result_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        result_label.configure(text=f"Added {result['added_count']} song(s) to the playlist!\n{result['missing']} songs were not evaluated.")
        result_btn.grid(row=1, column=0, padx=10, pady=10)
        result_btn.configure(command=lambda: webbrowser.open(result['playlist_url']))

#------------------------------------------App Config----------------------------------------------------------------------------

app = ctk.CTk()
app.geometry("700x650")
app.title("Spotify Genre Classifier")
app.resizable(False, False)
app._set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1) 

#------------------------------------------Title Config---------------------------------------------------------------------------

title_frame = ctk.CTkFrame(master=app, width=550, height=50, corner_radius=10, fg_color="#3682A2")
title_frame.grid(row=0, column=0, sticky="ew", pady=20, padx=20)

title_label = ctk.CTkLabel(
    master=title_frame, 
    text="Spotify Genre Classifier", 
    text_color="white", 
    font=("Cooper Black", 30, "bold")
)
title_label.place(rely=0.5, relx=0.5, anchor="center")

#------------------------------------------Source Config--------------------------------------------------------------------------------

source_frame = ctk.CTkFrame(master=app, width=650, height=60, fg_color="#242424")
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
source_opts.update(playlists)
# Set "values" to list(source_opts.keys())
source_dropdown = ctk.CTkComboBox(master=source_frame, values=list(source_opts.keys()), state="readonly")
source_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

#------------------------------------------Destination Config-------------------------------------------------------------------------

dest_frame = ctk.CTkFrame(master=app, width=650, height=80, fg_color="#242424")
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

new_playlist_entry = ctk.CTkEntry(master=dest_frame, placeholder_text="New playlist name")

dest_opts = {"Create New" : None}
dest_opts.update(playlists)
dest_dropdown = ctk.CTkComboBox(master=dest_frame, values=list(dest_opts.keys()), command=on_selection_change, state="readonly")
dest_dropdown.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

#------------------------------------------Genre Config-----------------------------------------------------------------------

gr_frame = ctk.CTkFrame(master=app, width=650, height=60, fg_color="#242424")
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

#------------------------------------------Classify Config------------------------------------------------------------------------

gen_btn=ctk.CTkButton(
    master=app,
    width=300, 
    height=40, 
    text="Classify Playlist", 
    text_color="white",
    font=("Arial Rounded MT Bold", 24, "bold"),
    fg_color="#3682A2",
    command=on_classify
)
gen_btn.grid(row=4, column=0, columnspan=2)

#------------------------------------------Result Config--------------------------------------------------------------------------------

result_frame = ctk.CTkFrame(master=app, width=650, height=100, fg_color="#242424")
result_frame.grid(row=5, column=0, sticky="ew", pady=20, padx=50)
result_frame.grid_propagate(False)
result_frame.grid_columnconfigure(0, weight=1)

prog_bar = ctk.CTkProgressBar(master=result_frame, mode="indeterminate")

result_btn = ctk.CTkButton(
    master=result_frame, 
    width=150,
    text="Open Playlist",
    text_color="white",
    font=("Arial Rounded MT Bold", 18, "bold"),
    fg_color="#3682A2",
    command=None
)

result_label=ctk.CTkLabel(
    master=result_frame,
    text="",
    text_color="white",
    font=("Arial Rounded MT Bold", 18, "bold")
)


app.mainloop()