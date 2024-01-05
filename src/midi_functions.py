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

def create_modified_midi(input_midi_file_path, output_midi_file_path, modified_note_pairs):
    # Load the original MIDI file
    original_midi_file = MidiFile(input_midi_file_path)

    # Create a new MIDI file
    modified_midi_file = MidiFile()

    # Copy metadata and other non-track information
    for i, track in enumerate(original_midi_file.tracks):
        if i == 0:
            modified_midi_file.tracks.append(track.copy())

    # Create a new track for modified notes
    modified_track = MidiTrack()
    modified_midi_file.tracks.append(modified_track)

    # Iterate through the modified note pairs and add corresponding note messages
    for msg in original_midi_file.tracks[1]:  # Assuming track 1 contains the notes
        if msg.type in {'note_on', 'note_off'}:
            note_number = msg.note
            velocity = msg.velocity
            time = msg.time

            # Find corresponding modified pair for the current note
            matching_pair = next(pair for pair in modified_note_pairs if pair[0] == time)
            modified_time = matching_pair[1]

            # Add modified note to the new track
            modified_track.append(Message(msg.type, note=note_number, velocity=velocity, time=modified_time))

    # Save the modified MIDI file
    modified_midi_file.save(output_midi_file_path)
