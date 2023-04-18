from Crypto import DES


def test_weak_key(key_hex):
    key = bytes.fromhex(key_hex)
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = b'TestData'

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext)

    # Check if the decrypted text is the same as the original plaintext
    return decrypted_text == plaintext


weak_keys = [
    '000000000000',
    'FFFFFFFFFFFF',
    '000000FFFFFF',
    'FFFFFF000000'
]

for i, key in enumerate(weak_keys):
    is_weak = test_weak_key(key)
    print(f"Key {i + 1} ({key}) is weak: {is_weak}")
