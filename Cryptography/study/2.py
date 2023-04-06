import numpy as np


def text_to_matrix(text):
    text = text.lower()
    text_matrix = [ord(c) - ord('a') for c in text]
    return np.array(text_matrix).reshape(-1, 1)


def matrix_to_text(matrix):
    text_matrix = matrix.flatten().tolist()
    text = ''.join([chr(int(x) % 26 + ord('a')) for x in text_matrix])
    return text


def hill_cipher(text, key_matrix):
    text_matrix = text_to_matrix(text)
    encrypted_matrix = np.dot(key_matrix, text_matrix) % 26
    return matrix_to_text(encrypted_matrix)


plaintext = "hill"
key_matrix = np.array([
    [8, 6, 9, 5],
    [6, 9, 5, 10],
    [5, 8, 4, 9],
    [10, 6, 11, 4]
])

ciphertext = hill_cipher(plaintext, key_matrix)
print("Ciphertext:", ciphertext)
