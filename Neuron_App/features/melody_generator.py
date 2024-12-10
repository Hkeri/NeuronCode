import customtkinter as ctk
from mido import MidiFile, MidiTrack, Message
import random
import settings
import os

def generate_melody(scale=[60, 62, 64, 65, 67, 69, 71, 72]):
    # Generate a random melody based on a given scale
    melody = []
    for _ in range(64):
        note = random.choice(scale)  # Choose a random note from the scale
        duration = random.randint(120, 480)  # Random duration for each note
        melody.append((note, duration))  # Store note and its duration
    return melody

def create_midi(melody, filename="neuron_gen_melody.mid"):
    # Create a MIDI file from a melody
    midi = MidiFile()  # Create a new MIDI file
    track = MidiTrack()  # Create a new track
    midi.tracks.append(track)  # Add the track to the MIDI file

    track.append(Message('program_change', program=0))  # Set the instrument (program change)
    
    for note, duration in melody:
        track.append(Message('note_on', note=note, velocity=100, time=0))  # Note on
        track.append(Message('note_off', note=note, velocity=100, time=duration))  # Note off

    midi.save(filename)  # Save the MIDI file
    print(f"MIDI file created: {filename}")  # Debug print statement

def play_midi():
    # Generate and play the MIDI melody based on selected scale
    scale = scale_var.get()
    scales = {
        "C Major": [60, 62, 64, 65, 67, 69, 71, 72],
        "A Natural Minor": [69, 71, 60, 62, 64, 65, 67],
        "A Harmonic Minor": [69, 71, 60, 62, 64, 65, 68],
        "D Major": [62, 64, 66, 67, 69, 71, 73],
        "D Natural Minor": [62, 64, 65, 67, 69, 70, 72],
        "D Harmonic Minor": [62, 64, 65, 67, 69, 70, 73],
        "E Natural Minor": [64, 66, 67, 69, 71, 72],
        "E Harmonic Minor": [64, 66, 67, 69, 71, 72, 75],
        "G Major": [67, 69, 71, 72, 74, 76],
        "G Natural Minor": [67, 69, 70, 72, 74, 75],
        "G Harmonic Minor": [67, 69, 70, 72, 74, 75, 78],
        "C Pentatonic": [60, 62, 64, 67, 69],
        "A Pentatonic": [69, 72, 74, 76, 79],
        "D Pentatonic": [62, 64, 67, 69, 71],
        "E Pentatonic": [64, 67, 69, 71, 74],
        "G Pentatonic": [67, 69, 71, 74, 76],
        "B Pentatonic": [71, 74, 76, 79, 81],
    }

    # Check if the selected scale is in the scales dictionary
    if scale in scales:
        melody = generate_melody(scales[scale])
        create_midi(melody)
        os.startfile("neuron_gen_melody.mid")
        print("Melody is being played!")
    else:
        print("Selected scale is not valid.")

# Create the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(f"{settings.dir_agi}\\images\\cyan.json")

root = ctk.CTk()
root.title("Melody Generator")
root.geometry("275x200")

# Create a label
label = ctk.CTkLabel(root, text="Choose a scale for the melody:")
label.pack(pady=10)

# Create a dropdown menu for scale selection
scale_var = ctk.StringVar()
scale_options = [
    "C Major", "A Natural Minor", "A Harmonic Minor", "D Major", 
    "D Natural Minor", "D Harmonic Minor", "E Natural Minor", "E Harmonic Minor", 
    "G Major", "G Natural Minor", "G Harmonic Minor", "C Pentatonic", 
    "A Pentatonic", "D Pentatonic", "E Pentatonic", "G Pentatonic", 
    "B Pentatonic"
]
scale_menu = ctk.CTkOptionMenu(root, values=scale_options, variable=scale_var)
scale_menu.pack(pady=10)

# Create a button to play the melody
play_button = ctk.CTkButton(root, text="Play Melody", command=play_midi)
play_button.pack(pady=20)

def main():
    root.mainloop()