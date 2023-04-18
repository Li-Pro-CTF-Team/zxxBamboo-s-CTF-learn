from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from binascii import unhexlify, hexlify

# Provided parameters
plaintext = b"today_is_tuesday"
key = unhexlify("0011223344556677")
iv = unhexlify("7766554433221100")
given_ciphertext = "cffffa20a73c667b45fec867850a70a382dad87e90ef16a1"

# Padding the plaintext to a multiple of 8 bytes (64 bits)
padded_plaintext = pad(plaintext, 8)

# Encrypt the plaintext using DES in CBC mode
cipher = DES.new(key, DES.MODE_CBC, iv)
ciphertext = cipher.encrypt(padded_plaintext)

# Convert the ciphertext to a hexadecimal string
ciphertext_hex = hexlify(ciphertext).decode()
print("ciphertext_hex:", ciphertext_hex)
print("given_ciphertext:", given_ciphertext)

# Compare the generated ciphertext with the given ciphertext
if ciphertext_hex == given_ciphertext:
    print("The ciphertexts match!")
else:
    print("The ciphertexts do not match.")
