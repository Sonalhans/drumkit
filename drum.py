import tkinter as tk
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()

def play_background_music():
    mixer.music.load("sounds/background_music.mp3")
    mixer.music.play(-1)  # Loop the music indefinitely

def stop_background_music():
    mixer.music.stop()

def play_sound(sound_file):
    mixer.music.load(sound_file)
    mixer.music.play()

def handle_click(event):
    key = event.widget.cget("text").lower()
    make_sound(key)

def make_sound(key):
    sound_map = {
        "w": "sounds/tom-1.mp3",
        "a": "sounds/tom-2.mp3",
        "s": "sounds/tom-3.mp3",
        "d": "sounds/tom-4.mp3",
        "j": "sounds/snare.mp3",
        "k": "sounds/crash.mp3",
        "l": "sounds/kick-bass.mp3"
    }
    if key in sound_map:
        play_sound(sound_map[key])

def show_drum_kit():
    # Stop background music
    stop_background_music()

    # Clear the welcome screen
    for widget in root.winfo_children():
        widget.destroy()
    
    # Title label
    title_label = tk.Label(root, text="Drum 🥁 Kit", font=("Arvo", 40), fg="#DBEDF3", bg="#283149")
    title_label.pack(pady=20)

    # Image map and buttons
    image_map = {
        "w": "images/tom1.png",
        "a": "images/tom2.png",
        "s": "images/tom3.png",
        "d": "images/tom4.png",
        "j": "images/snare.png",
        "k": "images/crash.png",
        "l": "images/kick.png"
    }

    buttons = []
    for key, img_path in image_map.items():
        img = Image.open(img_path)
        img = img.resize((100, 100), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        button = tk.Button(root, image=img, text=key.upper(), font=("Arvo", 15), compound="top",
                           width=120, height=120, bg="white", fg="#DA0463", bd=5)
        button.image = img  # Keep a reference to avoid garbage collection
        button.pack(side=tk.LEFT, padx=10)
        button.bind("<Button-1>", handle_click)
        buttons.append(button)

    # Key binding for keyboard interaction
    root.bind("<KeyPress>", lambda event: make_sound(event.char.lower()))

    # Footer label
    footer_label = tk.Label(root, text="Made with ❤️ by Sonal Hans.", font=("Arial", 12), fg="#DBEDF3", bg="#283149")
    footer_label.pack(side=tk.BOTTOM, pady=20)

def show_welcome_screen():
    # Play background music
    play_background_music()

    # Welcome screen design
    welcome_label = tk.Label(root, text="Welcome to the Drum Kit 🥁", font=("Cursive", 50), fg="#DBEDF3", bg="#283149")
    welcome_label.pack(pady=100)

    # Play button
    play_button = tk.Button(root, text="Play",bg="#DA0463", fg="black", command=show_drum_kit)
    play_button.pack(pady=50)

    footer_label = tk.Label(root, text="Made with ❤️ by Sonal Hans.", font=("Arial", 12), fg="#DBEDF3", bg="#283149")
    footer_label.pack(side=tk.BOTTOM, pady=20)
    
# Main window setup
root = tk.Tk()
root.title("Drum Kit")
root.geometry("1500x800")
root.config(bg="#283149")

# Show the welcome screen on startup
show_welcome_screen()

root.mainloop()