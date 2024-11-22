import random
from midiutil import MIDIFile
from keys import get_key
import chord_progressions as cp

def create_melody(filename="random_melody.mid", track=0, channel=0, tempo=120, duration=1, length=16, scale=1):
    # Create a MIDI object with 1 track
    midi = MIDIFile(1)
    midi.addTempo(track, 0, tempo) # Add tempo to the track

    # Randomize the key
    #notes = []
    #notes.append(random.randint(60,96))

    notes = get_key(random.randint(60,96), scale)
    #i = 1
    #while len(notes) < 7:
    #    if i == 3:
    #        notes.append(notes[i-1] + 1)
    #    else:
    #        notes.append(notes[i-1] + 2)
    #    i += 1

    time = 0 # Start time for the first note
    measure = 0
    intervals = [1, 2, 4]
    # Decide how long you want the song
    # How many notes and how long they are
    while measure < length:
        chord = cp.get_chord(scale, notes, measure % 4)
        bass = [tone - 24 for tone in chord]
        note = random.choice(chord) # Pick a random note from the right chord
        velocity = random.randint(30, 100) # Random velocity (volume)
        
        duration=random.choice(intervals)
        midi.addNote(track, channel, note, time, duration, velocity)
        # Add a root chord
        if time % 4 == 0 or time == 0:
            midi.addNote(track, channel, random.choice(chord), time, duration, velocity)
            midi.addNote(track, channel, random.choice(chord), time, duration, velocity)
            
        for i in range(duration):
            if length * 4 == time:
                break
            time += 1
            if time % 4 == 0:
                measure += 1
            if time % 4 == 0 or time == 0:
                for n in bass:
                    midi.addNote(track, channel, n, time, 4, velocity)
        

    
    # Write the MIDI data to a file
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)
    
    #print(f"Melody saved to {filename}")
    return filename