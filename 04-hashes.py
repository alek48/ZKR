import hashlib
from time import process_time
import sys


def generate_hashes_verbose(input_data):
    data = input_data.encode('UTF-8')
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()
    sha3_224 = hashlib.sha3_224()
    sha3_256 = hashlib.sha3_256()
    sha3_384 = hashlib.sha3_384()
    sha3_512 = hashlib.sha3_512()
    hashes = [md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512]
    for elem in hashes:
        elem.update(data)

    return {"original": input_data,
            "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(),
            "sha224": sha224.hexdigest(),
            "sha256": sha256.hexdigest(),
            "sha384": sha384.hexdigest(),
            "sha512": sha512.hexdigest(),
            "sha3_224": sha3_224.hexdigest(),
            "sha3_256": sha3_256.hexdigest(),
            "sha3_384": sha3_384.hexdigest(),
            "sha3_512": sha3_512.hexdigest()
            }

if len(sys.argv) > 1:
    data = sys.argv[1]
else:
    data = "Placeholder sequence to hash."

hashes = generate_hashes_verbose(data)

print("\n" + "Hash".ljust(10), "Bytes".ljust(7), "Value", "\n---")
for item in hashes.items():
    print(item[0].ljust(10), str(len(item[1])*4).ljust(7), item[1])

