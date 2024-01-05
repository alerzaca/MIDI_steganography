import os
import random
from midi_functions import extract_note_info, calculate_randrange
from text_functions import ascii_to_pairs

# Parameters
RAND_PERCENTAGE = 2.5
MIDI_FILE = 'Beethoven_Fur_Elise.mid'
PLAINTEXT = "Hello, World!"

def encode_pair(midi_pair, movement_pair, randrange):
    n = random.randrange(1, randrange+1)
    m = random.randrange(1, randrange+1)

    x = 0
    y = 0
    if movement_pair[0] == 0:
        x = midi_pair[0]
    elif movement_pair[0] == 1:
        x = midi_pair[0] - n
    else:
        x = midi_pair[0] + n

    if movement_pair[1] == 0:
        y = midi_pair[1]
    elif movement_pair[1] == 1:
        y = midi_pair[1] - n
    else:
        y = midi_pair[1] + n

    return [x, y]

def encode(midi_pairs, movement_pairs, randrange):
    encoded_pairs = []
    for i in range(len(movement_pairs)):
        pair = encode_pair(midi_pairs[i], movement_pairs[i], randrange)
        encoded_pairs.append(pair)
    
    return encoded_pairs

def decode():
    return


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    midi_file_path = os.path.join(current_dir, '..', 'MIDIs', MIDI_FILE)

    randrange = calculate_randrange(midi_file_path, RAND_PERCENTAGE)

    midi_pairs = extract_note_info(midi_file_path)
    movement_pairs = ascii_to_pairs(PLAINTEXT)

    print("ASCII:", PLAINTEXT)
    print("Pair list:", movement_pairs)
    print("Randrange: ", randrange)

    print(midi_pairs)
    encoded_midi = encode(midi_pairs, movement_pairs, randrange)
    print(encoded_midi)

if __name__ == "__main__":
    main()