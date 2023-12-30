import statistics
import os
import mido
from mido import MidiFile, MidiTrack

def extract_note_info(midi_file_path):
    note_pairs = []
    midi_file = MidiFile(midi_file_path)
    active_notes = {}  # Dictionary to store currently active notes: {note_number: start_time}

    for i, track in enumerate(midi_file.tracks):
        time = 0
        for msg in track:
            time += msg.time

            if msg.type == 'note_on' and msg.velocity != 0:
                # Note on - start a note
                active_notes[msg.note] = time
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                # Note off or note on with zero velocity - end a note
                if msg.note in active_notes:
                    note_pairs.append([active_notes[msg.note], time])
                    del active_notes[msg.note]

        # For now it takes only the first track
        return note_pairs


def calculate_randrange(midi_file_path, percentage=10):
    note_pairs = extract_note_info(midi_file_path)

    if not note_pairs:
        raise ValueError("No note information found in the MIDI file.")

    durations = [end - start for start, end in note_pairs]
    average_duration = statistics.mean(durations)
    shift_range = int(percentage / 100 * average_duration)

    return shift_range
