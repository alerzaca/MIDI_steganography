import os
from text_functions import calculate_offsets
from midi_functions import extract_note_info, encode_midi, decode_midi

# Parameters
RANDRANGE = 7
MIDI_FILE = 'Beethoven_Fur_Elise.mid'
PLAINTEXT = "Hello, World!"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    original_midi_file_path = os.path.join(current_dir, '..', 'MIDIs', MIDI_FILE)
    
    offset_array = calculate_offsets(PLAINTEXT, RANDRANGE)
    # offset_array = calculate_offsets(PLAINTEXT, RAND_PERCENTAGE)

    modified_midi_file_path = os.path.join(current_dir, '..', 'MIDIs', 'Modified_' + MIDI_FILE)
    encode_midi(original_midi_file_path, modified_midi_file_path, offset_array)

    print("Offsets calculated from given plaintext:")
    print(offset_array)
    print('\n')

    print("Original notes positions:")
    original_pos = extract_note_info(original_midi_file_path)
    print(original_pos)
    print('\n')

    print("Modified notes positions:")
    encoded_pos = extract_note_info(modified_midi_file_path)
    print(encoded_pos)
    print('\n')

    decoded_offests = decode_midi(original_pos, encoded_pos)

    print("Offsets re-calculated from encoded midi:")
    print(decoded_offests)
    print('\n')

if __name__ == "__main__":
    main()