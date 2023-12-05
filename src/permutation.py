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

def nonal_to_binary(nonal_number):
    nonal_digits = [int(digit) for digit in str(nonal_number)]
    decimal_number = sum(digit * (9 ** idx) for idx, digit in enumerate(reversed(nonal_digits)))
    return bin(decimal_number)[2:]

def binary_to_nonal(binary_number):
    decimal_number = int(str(binary_number), 2)
    nonal_digits = []
    while decimal_number > 0:
        nonal_digit = decimal_number % 9
        nonal_digits.insert(0, str(nonal_digit))
        decimal_number //= 9

    return ''.join(nonal_digits) if nonal_digits else '0'

'''
nonal_input = 545345364235
binary_result = nonal_to_binary(nonal_input)
print(f"Nonal {nonal_input} in binary: {binary_result}")

binary_input = "010110011010101"
nonal_result = binary_to_nonal(binary_input)
print(f"Binary {binary_input} in nonal: {nonal_result}")

def permutation_test(permutation):
    result = map_permutation_to_number(permutation)

    if result is not None:
        print(f"The permutation {permutation} corresponds to the number {result.value}")
    else:
        print(f"No equivalent for the permutation {permutation}")

permutation_test((1,2))
'''