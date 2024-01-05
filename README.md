# MIDI Steganography
Audio steganography - using shifts in MIDI quantization as a message carrier

<br />

## Software used
- [Ableton 11 Live](https://www.ableton.com) for midi tracks visualisation
- [MuseScore 4](https://musescore.org) for scores
- Python with [mido](https://pypi.org/project/mido/) library

All sheet music used for testing is under a CC BY or CC0 license and is free to share and modify.

<br />

## How it works
### Encoding
1. Extract all note_on/note_off info from a given MIDI file and pack them in pairs. *Warning: this will work properly only for tracks containing one note at a time, otherwise notes will overlap*.
   
```
beg: 960, end: 1187
(960, 1187)
```

2. Translate given plaintext (or ciphertext encoded beforehand) to **base-9**.
   
3. Translate the received base-9 text to list of pairs representing the neeeded movement of a note.
   Can be done as translating simply between base-9 and base-3 or permutations may be assigned differently, but then it has to be hardcoded.

```
1 = ZERO_ONE
(0, 1): Permutation.ZERO_ONE

2 = ZERO_TWO
(0, 2): Permutation.ZERO_TWO

...

7 = TWO_ONE
(2, 1): Permutation.TWO_ONE

8 = TWO_TWO
(2, 2): Permutation.TWO_TWO
```

4. Calculate the offsets of new notes using the movement pair. The offset will be set randomly in predefined range.
   The minimal offset is 1 (not including offset 0 that is unchanged), because midi ticks are integers. Maximum has to be calculated separetely in order to keep it flexible and yet inaudible.
   
```
0 => 0
1 => random forward movement
2 => random backward movement

movement (0,1)
would give x = 0 and y = negative random int

movement (0,2)
would give x = 0 and y = positive random int
```

5. Use calculated random movement to modify **Delta Times** of original MIDI file and export encoded track to a new MIDI.

```
for each pair:

message 0: beginning of a note (note_on event)
message 1: end of a note (note_off event)
message 2: beginning of the next note (note_on), adjusted to its original position to hold the rest of the track in place
```

<br />

### Decoding
1. Extract all note_on/note_off info from both encoded and original MIDI file and pack them in pairs.
   *Warinig: hence, you must have access to the original MIDI or its score.*

2. Compare encoded and original pairs to recalculate the movement pairs.

```
(original_X - modified_x, modified_y - original_x)
```
 
3. Translate the list of pairs to base-9 and then to binary/ASCII/whatever to get the original plaintext.

<br />

## Future improvements
```
- Rebuild the program structure (organise all into classes etc.)
- Implement appropriate encoding for tracks with overlapping notes
- Implement encoding for multiple notes at a time (chords encoding)
- Build usage interface (get rid of hardcoded plaintext, file paths etc.)
- Implement randrange determining algorithm
- Make the code more readable
```


