# purpose: Learn python, use Git
# date: 28-JUN-2020
# author: David Kopec - "Classic Computer Science Problems in Python" - Manning

from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:     # generate random sequence of bytes of specified length
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")     # convert bytes to string and return string
def encrypt(original: str) ->  Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int  = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy   # apply XOR
    return dummy, encrypted
def decrypt(key1: int, key2: int) ->  str:
    decrypted: int = key1 ^ key2            # apply XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

    