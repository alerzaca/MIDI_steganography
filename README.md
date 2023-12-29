# MIDI Steganography
Audio steganography - using shifts in MIDI quantization as a message carrier

This repository has not been built yet, but sooner or later it will contain a full description and hopefully working programs that perform encoding and decoding messages in midi files.

The algorithms used here are not inspired by any specific existing audio steganography algorithms, but it requires further research whether such a method has ever been invented and/or implemented.

<br />

## Software used
- [Ableton 11 Live](https://www.ableton.com) for midi tracks visualisation
- [MuseScore 4](https://musescore.org) for scores
- Python with [mido](https://pypi.org/project/mido/) library

All sheet music used for testing is under a CC BY or CC0 license and is free to share and modify.

<br />

## How it works
### Encoding
1. Extract note_on and note_off info from a given MIDI file.
   
<pre><code>beg: 960, end: 1187</code></pre>

2. Pack them in pairs,
   *warning: this will work properly only for tracks containing one note at a time, otherwise notes will overlap*.

<pre><code>(960, 1187)</code></pre>

3. Translate given plaintext (or ciphertext encoded beforehand) to base-9.
   
4. Translate the received base-9 text to list of pairs representing the neeeded movement of a note.

<pre><code>1 = ZERO_ONE
(0, 1): Permutation.ZERO_ONE</code></pre>

5. Calculate the positions of new notes using original note pair and the movement pair. The offset will be set randomly in predefined range
   (to do: define range automatically by average note length and fitting to the tempo).
   
<pre><code>(960, 1187) with movement (0,1)
would give x = 0 and y = negative random int

(960, 1187) with movement (0,2)
would give x = 0 and y = positive random int

then output can be calculated: (960 + x, 1187 + y)
</code></pre>

6. Having created a new list of notes, export them into encoded MIDI file.

<br />

### Decoding
1. Extract note_on and note_off info from an encoded MIDI file and pack them into pairs the same way as for encoding
   
2. Repeat the same for the original MIDI file, *warinig: hence, you must have access to the original MIDI or score*.

3. Compare received lists of pairs and reverse the calculating process (point 5. in encoding) to get the movement pairs.
 
4. Translate the list of pairs to base-9 and then to binary/ASCII/whatever to get the original plaintext.

