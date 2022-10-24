from tkinter import *
import pygame
from tkinter import filedialog
import soundfile as sf
import pyloudnorm as pyln

root = Tk()
root.title('Wav Player')
root.geometry("500x300")

#initialize Pygame Mixer
pygame.mixer.init()

#Add song function
def add_song():
	song = filedialog.askopenfilename(initialdir='', title="Choose a song", filetypes=(("wav files", "*.wav"), ))
	song = song.replace("/Users/macintosh/", "")
	song = song.replace(".wav", "")
	
	#Add song to listbox
	song_box.insert(END, song, "{:.2f}".format(loudness) + " Lufs", rate)


# Play selected song
def play():
	song = song_box.get(ACTIVE)
	song = f'/Users/macintosh/{song}.wav'


	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

# Stop playing 
def stop():
	pygame.mixer.music.stop()
	song_box.seletion_clear(ACTIVE)


data, rate = sf.read("test.wav") # load audio


# measure the loudness first 
meter = pyln.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data)



# Create Playlist Box
song_box = Listbox(root, bg= "black", fg="grey", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Create Player control buttons images
back_btn_img = PhotoImage(file='back.gif')
forward_btn_img = PhotoImage(file='forward.gif')
play_btn_img = PhotoImage(file='play.gif')
pause_btn_img = PhotoImage(file='pause.gif')
stop_btn_img = PhotoImage(file='stop.gif')

# Player Control frame
controls_frame = Frame(root)
controls_frame.pack()

# Player Control Button
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, padx=10)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, padx=10)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, padx=10, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, padx=10)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, padx=10, command=stop)

back_button.grid(row=0, column=0)  
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add Song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One song", command=add_song)


root.mainloop()