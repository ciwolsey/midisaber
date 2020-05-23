## ** NO LONGER MAINTAINED **

# MidiSaber
MidiSaber can convert a MIDI file into the json format used by BeatSaber. Midi is used to define the timing of your beatmap which can then be imported to a new online editor which allows you 'step through' the timings to define position and cut etc.

# Usage
Load up your favourite audio software, and create a midi clip with a single note to define the rhythm, Any note will do. Export the midi file and then convert it as follows:
```
MidiSaber <MidiFile>
```
The converted JSON will be placed in your clipboard.

Alternatively you can drag your midi file onto MidiSaber.exe.

MidiSaber will prompt you for a BPM. This is the BPM you used when creating the midi file. Midi conversion is performed in real time so if your song is two minutes long conversion will take two minutes. MidiSaber only supports track midi (midi type 0).

# MidiSaber online editor
Once conversion completes the resulting JSON will be copied to your clipboard. Paste this into your beatmap and then load the map into your favourite editor.
MidiSaber can be used with any editor, but is intended to be used with it's owned editor that you can find at:
https://beatmapper.surge.sh - Just import your song and the JSON, edit away and when done hit export and copy it back out into your beatmap.

You can load any song you like into the online editor, but it is intended to be used alongside the midi converter.

# Videos
[Creating MIDI for MidiSaber](https://www.youtube.com/watch?v=y1CPDLij8ys&feature=youtu.be)


