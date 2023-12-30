import os
from midi_functions import extract_note_info, calculate_randrange
from text_functions import ascii_to_pairs

# Parameters
RAND_PERCENTAGE = 2.5
MIDI_FILE = 'Beethoven_Fur_Elise.mid'
PLAINTEXT = "Hello, World!"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    midi_file_path = os.path.join(current_dir, '..', 'MIDIs', MIDI_FILE)

    randrange = calculate_randrange(midi_file_path, RAND_PERCENTAGE)

    midi_pairs = extract_note_info(midi_file_path)
    for pair in midi_pairs:
        print(pair)

    result_list = ascii_to_pairs(PLAINTEXT)

    print("ASCII:", PLAINTEXT)
    print("Pair list:", result_list)
    print("Randrange: ", randrange)

if __name__ == "__main__":
    main()