from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from binascii import unhexlify, hexlify

# Provided parameters
plaintext = b"today_is_tuesday_helloworld"
key = unhexlify("00112233445566770011223344556677")
iv = unhexlify("77665544332211007766554433221100")
given_ciphertext = "6d8e688ec4104ede9e925f49df4eaf79f1cfd4155cc5a15b48e73cda91adefa0"

# Padding the plaintext to a multiple of 16 bytes (128 bits)
padded_plaintext = pad(plaintext, 16) 

# Encrypt the plaintext using AES in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)
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
