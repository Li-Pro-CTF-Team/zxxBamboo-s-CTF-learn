import re
from collections import Counter
from math import gcd
from functools import reduce


def kasiski_test(ciphertext):
    ciphertext = str(ciphertext)
    # Find repeating sequences of 3 or more characters in the ciphertext
    repeating_sequence = "CHR"
    count = ciphertext.count(repeating_sequence)
    print("Occurrences of 'CHR':", count)

    # Calculate the distance between the repeating sequences
    indices = [m.start() for m in re.finditer(repeating_sequence, ciphertext)]
    # Calculate the distances between the indices
    distances = [indices[i + 1] - indices[i] for i in range(len(indices) - 1)]
    print('distances:', distances)

    # Determine the greatest common divisor of the distances
    if not distances:
        key_length = 0
    else:
        key_length = reduce(gcd, distances)
    return key_length


def frequency_analysis(ciphertext, key_length):
    freqs = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    decrypted_key = ''

    for i in range(key_length):
        # Group the ciphertext by key length
        segment = ciphertext[i::key_length]

        # Count the occurrences of each letter in the segment
        letter_freq = Counter(segment)

        # Find the most common letter in the segment
        most_common = letter_freq.most_common(1)[0][0]

        # Estimate the key character by comparing the most common letter with English letter frequencies
        key_char = chr(((ord(most_common) - ord('A')) - (ord(freqs[0]) - ord('A'))) % 26 + ord('A'))
        decrypted_key += key_char

    return decrypted_key


def vigenere_cipher(ciphertext, key, encrypt=True):
    key_len = len(key)
    key_ints = [ord(i) for i in key]
    ciphertext_ints = [ord(i) for i in ciphertext]
    result = ''
    for i, c in enumerate(ciphertext_ints):
        key_int = key_ints[i % key_len]
        if encrypt:
            new_c = (c + key_int) % 26
        else:
            new_c = (c - key_int) % 26
        result += chr(new_c + ord('A'))
    return result


with open('ciphertext.txt', 'rb') as f:
    ciphertext = f.read()
    ciphertext = ciphertext.decode('utf-8')
# 1. Use the Kasiski test to determine the key length
key_length = kasiski_test(ciphertext)
print("Key length:", key_length)

# 2. Use frequency analysis and the Kasiski test to crack the Vigenère cipher
# 3. Decrypt the ciphertext using the found key
if key_length == 0:
    print("Failed to determine key length")
else:
    key = frequency_analysis(ciphertext, key_length)
    print("Key:", key)
    plaintext = vigenere_cipher(ciphertext, key, encrypt=False)
    print("Plaintext:", plaintext)
