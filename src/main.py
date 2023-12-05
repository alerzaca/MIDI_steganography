import os
import mido
from mido import MidiFile

'''
Note: Many MIDI files will encode note offs as note ons with velocity zero.
eg. "note_on channel=0 note=76 velocity=64 time=960
     note_on channel=0 note=76 velocity=0 time=227"
'''

def extract_note_info(midi_file_path):
    midi_file = MidiFile(midi_file_path)
    time = 0

    # works properly for one note at a time

    for i, track in enumerate(midi_file.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            time += msg.time
            if msg.type == 'note_on':
                if msg.velocity != 0:
                    print(f"beg: {time}, ", end="")
                else:
                    print(f"end: {time}\n")
            elif msg.type == 'note_off':
                print(f"end: {time}\n")
            else:
                print("Error fetching note info..")
        
        print(f"duration: {midi_file.length} seconds")
        print(f"tick time: {midi_file.length / time} seconds")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    midi_file_path = os.path.join(current_dir, '..', 'MIDIs', 'Beethoven_Fur_Elise.mid')

    extract_note_info(midi_file_path)

if __name__ == "__main__":
    main()