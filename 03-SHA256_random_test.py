from hashlib import sha256
from random import randint
from os import urandom
from itertools import zip_longest

ITERATIONS = 1_000_000


def XOR(a, b):
    return bytes(x ^ y for x, y in zip_longest(a, b, fillvalue=0))


def int2bytes(value):
    byte_list = []
    while value != 0:
        byte_list.append(value % 256)
        value //= 256
    byte_list.reverse()
    return bytes(byte_list)


def count_one_bits(a):
    a = int.from_bytes(a, 'little')
    counter = 0
    while a != 0:
        counter += (a % 2)
        a //= 2
    return counter


changes = []
for _ in range(ITERATIONS):
    data = urandom(32)
    first_hash = sha256(data).digest()

    bit_to_change = 2**randint(0, 255)
    XOR_mask = int2bytes(bit_to_change).rjust(32, b'\00')

    one_off_data = XOR(data, XOR_mask)
    second_hash = sha256(one_off_data).digest()

    changed_bits = XOR(first_hash, second_hash)
    num_of_changes = count_one_bits(changed_bits)
    changes.append(num_of_changes)

min_changed = min(changes)
avg_changed = sum(changes)/len(changes)
max_changed = max(changes)

print("\nSrednia liczba zmienionych bitów skrótu przy zmianie jednego bitu wejścia (wykonano {} iteracji):".format(ITERATIONS))
print("minimalnie:".ljust(13), "{:.2f}".format(float(min_changed)).rjust(6), "{:.2f}%".format(min_changed*100/256))
print("Średnio:".ljust(13), "{:.2f}".format(float(avg_changed)).rjust(6), "{:.2f}%".format(avg_changed*100/256))
print("Maksymalnie:".ljust(13), "{:.2f}".format(float(max_changed)).rjust(6), "{:.2f}%".format(max_changed*100/256))
