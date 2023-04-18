from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from binascii import unhexlify, hexlify


def generate_subkeys(key):
    des = DES.new(key, DES.MODE_ECB)
    c = des.encrypt(pad(b'0' * 8, 8))
    d = des.decrypt(c)
    return (c, d)


def check_weak_key(key):
    c, d = generate_subkeys(key)
    return c == d


def check_semi_weak_keys(key1, key2):
    c1, d1 = generate_subkeys(key1)
    c2, d2 = generate_subkeys(key2)
    return c1 == d2 and c2 == d1


# Provided keys
keys = [
    unhexlify("0000000000000000"),
    unhexlify("00FF00EFF0FF00FF"),
    unhexlify("00FF00E100FF00FF"),
    unhexlify("E1E1E1E1F0F0F0F0")
]

for key in keys:
    if check_weak_key(key):
        print(f"Key {key.hex()} is a weak key.")
    elif any(check_semi_weak_keys(key, other_key) for other_key in keys if other_key != key):
        print(f"Key {key.hex()} is a semi-weak key.")
    else:
        print(f"Key {key.hex()} is neither weak nor semi-weak.")
