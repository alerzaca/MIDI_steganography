from enum import Enum

'''
ZERO [0] corresponds to the same position as the original
ONE [1] corresponds to the position shifted forward relative to the original
TWO [2] corresponds to the position shifted backward relative to the original
'''

class Permutation(Enum):
    ZERO_ZERO = 0
    ZERO_ONE = 1
    ZERO_TWO = 2

    ONE_ZERO = 3
    ONE_ONE = 4
    ONE_TWO = 5

    TWO_ZERO = 6
    TWO_ONE = 7
    TWO_TWO = 8


def map_permutation_to_number(permutation):
    permutation_mapping = {
        (0, 0): Permutation.ZERO_ZERO,
        (0, 1): Permutation.ZERO_ONE,
        (0, 2): Permutation.ZERO_TWO,
        (1, 0): Permutation.ONE_ZERO,
        (1, 1): Permutation.ONE_ONE,
        (1, 2): Permutation.ONE_TWO,
        (2, 0): Permutation.TWO_ZERO,
        (2, 1): Permutation.TWO_ONE,
        (2, 2): Permutation.TWO_TWO,
    }
    
    return permutation_mapping.get(permutation, None)


def base9_to_binary(nonal_number):
    nonal_digits = [int(digit) for digit in str(nonal_number)]
    decimal_number = sum(digit * (9 ** idx) for idx, digit in enumerate(reversed(nonal_digits)))
    return bin(decimal_number)[2:]


def binary_to_base9(binary_number):
    decimal_number = int(str(binary_number), 2)
    nonal_digits = []
    while decimal_number > 0:
        nonal_digit = decimal_number % 9
        nonal_digits.insert(0, str(nonal_digit))
        decimal_number //= 9

    return ''.join(nonal_digits) if nonal_digits else '0'


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


def ascii_to_pairs(text):
    base9_value = ascii_to_base9(text)
    
    permutation_list = [int(digit) for digit in base9_value]

    pairs = []
    for perm_number in permutation_list:
        pair = [perm_number // 3, perm_number % 3]
        pairs.append(pair)

    return pairs

# Test/example
text_to_convert = "Hello, World!"
base9_result = ascii_to_base9(text_to_convert)
ascii_result = base9_to_ascii(base9_result)

print("ASCII:", text_to_convert)
print("Base-9:", base9_result)
print("Decoded ASCII:", ascii_result)

binary_to_convert = "1101101010101101101"
base9_result = binary_to_base9(binary_to_convert)
binary_result = base9_to_binary(base9_result)

print("\nBinary:", binary_to_convert)
print("Base-9:", base9_result)
print("Decoded binary:", binary_result)