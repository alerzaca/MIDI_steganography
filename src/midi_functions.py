from mido import MidiFile, MidiTrack, Message

def extract_note_info(midi_file_path):
    note_pairs = []
    midi_file = MidiFile(midi_file_path)
    active_notes = {}  # Dictionary to store currently active notes: {note_number: start_time}

    for i, track in enumerate(midi_file.tracks):
        time_ctr = 0
        for msg in track:
            time_ctr += msg.time

            if msg.type == 'note_on' and msg.velocity != 0:
                # Note on - start a note
                active_notes[msg.note] = time_ctr
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                # Note off or note on with zero velocity - end a note
                if msg.note in active_notes:
                    note_pairs.append([active_notes[msg.note], time_ctr])
                    del active_notes[msg.note]

        # For now it takes only the first track
        return note_pairs
    

def encode_midi(input_midi_file_path, output_midi_file_path, offset_array):
    midi_file = MidiFile(input_midi_file_path)
    new_midi_file = MidiFile(ticks_per_beat=midi_file.ticks_per_beat)

    # For now it takes only the first track
    original_track = midi_file.tracks[0]
    new_track = MidiTrack()
    messages = []
    checksum = 0

    for msg in original_track:
        if msg.type in ['note_on', 'note_off']:
            messages.append([msg.type, msg.channel, msg.note, msg.velocity, msg.time])

    for i in range(len(offset_array)):
        pair = offset_array[i]
        x = pair[0]
        y = pair[1]

        if messages[2*i][0] == 'note_on':
            messages[2*i][4] -= x    
        if messages[2*i + 1][0] == 'note_off' or messages[2*i + 1][3] == 0:
            messages[2*i + 1][4] += x + y
        if messages[2*i + 2][0] == 'note_on':
            messages[2*i + 2][4] -= y
        
    for msg in messages:
        new_track.append(Message(msg[0], channel=msg[1], note=msg[2], velocity=msg[3], time=msg[4]))

    new_midi_file.tracks.append(new_track)
    new_midi_file.save(output_midi_file_path)

def decode_midi(original_positions, modified_positions):
    decoded = []
    for i in range(len(modified_positions)):
        x = modified_positions[i][0]
        y = modified_positions[i][1]

        decoded.append([original_positions[i][0] - x, y - original_positions[i][1]])
    
    return decoded