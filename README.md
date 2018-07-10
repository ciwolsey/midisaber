# MidiSaber
MidiSaber can convert a MIDI file into the json format used by BeatSaber. Midi is used to define the timing of your beatmap which can then be imported to a new online editor which allows you 'step through' the timings to define position and cut etc.

# Usage
Load up your favourite audio software, and create a midi clip with a single note to define the rhythm, Any note will do. Export the midi file and then convert it as follows:
```
MidiSaber <MidiFile>
```
MidiSaber will prompt you for a BPM. This is the BPM you used when creating the midi file. Midi converion is performed in real time so if your song is 2 minutes long conversion will take 2 minutes.

# MidiSaber online editor

Once conversion completes the resulting JSON will be copied to your clipboard. Paste this into your beatmap and then load the map into your favourite editor.
MidiSaber can be used with any editor, but is intended to be used with it's owned editor that you can find at:
https://beatmapper.surge.sh - Just import your song and the JSON, edit away and when done hit export and copy it back out into your beatmap.
