# external deps: mido, pyperclip, pyglet
import pyperclip
import mido
# Built in deps
import argparse
from mido import MidiFile
import sys
from random import randint
import copy
import json
import structures

# Generates left and right hand notes in set positions
def GenerateStaticNotes():
    # Left Hand Note
    left_note = copy.deepcopy(structures.note)
    left_note["_time"] = song_tick_pos
    left_note["_type"] = 0
    left_note["_lineIndex"] = 1
    left_note["_lineLayer"] = 1
    # Right Hand Note
    right_note = copy.deepcopy(structures.note)
    right_note["_time"] = song_tick_pos
    right_note["_type"] = 1
    right_note["_lineIndex"] = 2
    right_note["_lineLayer"] = 1
    # Return l/r notes as an array
    return [left_note, right_note]

# Set BPM to 60 in BeatSaber
mid = MidiFile(sys.argv[1])

# Check midi type is 0 / track
if mid.type != 0:
    print("Only midi track (type 0) are supported, exiting")
    exit()

# Request BPM from user
target_bpm  = int(input("BPM: "))

# Create a beatmap from shell
beatmap = copy.deepcopy(structures.map)
beatmap["_beatsPerMinute"] = target_bpm

# Current position in song
song_tick_pos = 0
last_tick_pos = -1

print("Converting...")
sys.stdout.write('[')
sys.stdout.flush()

# Play through midi converting each midi note to a beatsaber note
for i in enumerate(mid.play()):
    song_tick_pos += i[1].time * 2
    if i[1].type == "note_on":
        for note in GenerateStaticNotes():
            beatmap["_notes"].append(note)
            sys.stdout.write('-')
            sys.stdout.flush()
sys.stdout.write(']')
sys.stdout.flush()

# Copy pretty formatted JSON to clipboard and notify user
pyperclip.copy(json.dumps(beatmap, indent=4))

print('\n\nFinished. Map copied to clipboard\n')
