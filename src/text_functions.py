import random

def encode_pair(pair, randrange):    
    x = 0
    y = 0
    
    n = random.randrange(1, randrange+1)
    if pair[0] == 1:
        x = -n
    if pair[0] == 2:
        x = n

    m = random.randrange(1, randrange+1)
    if pair[1] == 1:
        y = -n
    if pair[1] == 2:
        y = n

    return [x, y]

def ascii_to_base9(text):
    base9_list = []

    for char in text:
        ascii_value = ord(char)
        base9_value = ""
        
        while ascii_value > 0:
            remainder = ascii_value % 9
            base9_value = str(remainder) + base9_value
            ascii_value //= 9
        
        base9_list.append(base9_value.zfill(3))

    return ''.join(base9_list)


def base9_to_ascii(base9_text):
    ascii_text = ""

    for i in range(0, len(base9_text), 3):
        base9_chunk = base9_text[i:i+3].lstrip('0')
        if not base9_chunk:
            base9_chunk = '0'
        decimal_value = int(base9_chunk, 9)
        ascii_text += chr(decimal_value)

    return ascii_text


def calculate_offsets(text, randrange):
    base9_value = ascii_to_base9(text)
    
    permutation_list = [int(digit) for digit in base9_value]

    pairs = []
    for perm_number in permutation_list:
        pair = [perm_number // 3, perm_number % 3]
        pairs.append(encode_pair(pair, randrange))

    return pairs