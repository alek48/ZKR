from hashlib import md5
from os import urandom

iterations = 1_000_000
collision_times = []
for _ in range(iterations):
    i = 0
    bits_list = []
    while True:
        i += 1
        data = urandom(128)
        hash_head = md5(data).hexdigest()[:3]
        if hash_head not in bits_list:
            bits_list.append(hash_head)
        else:
            collision_times.append(i)
            break
print("\nLiczba skrótów potrzebna do kolizji na pierwszych 12 bitach (wykonano {} iteracji):".format(iterations))
print("minimalnie: {}".format(min(collision_times)))
print("Średnio: {}".format(sum(collision_times)/len(collision_times)))
print("Maksymalnie: {}".format(max(collision_times)))
