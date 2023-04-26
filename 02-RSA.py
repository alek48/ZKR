from sympy import randprime


MIN_VAL = 10**3
MAX_VAL = 10**4


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def generate_key(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    while True:
        e = randprime(MIN_VAL, MAX_VAL)
        if is_coprime(e, phi):
            break
    d = pow(e, -1, phi)
    return ((e, n), (d, n))


def encrypt_message(message, key):
    e, n = key
    out = []
    for elem in message:
        out.append(pow(ord(elem), e, n))
    return out


def decrypt_message(message, key):
    d, n = key
    out = []
    for elem in message:
        out.append(pow(elem, d, n))
    return "".join(chr(x) for x in out)


def main():
    p, q = (30097, 50411)
    p = randprime(MIN_VAL, MAX_VAL)
    q = randprime(MIN_VAL, MAX_VAL)
    print(p, q)
    public_key, private_key = generate_key(p, q)
    print(f'klucz publiczny: {public_key}')
    print(f'Klucz prywatny: {private_key}')
    message = 'Jakaś długa wiadomość do zaszyfrowania i odszyfrowania używając RSA.'
    print(f'Oryginalna wiadomość: {message}')
    encrypted = encrypt_message(message, public_key)
    print(f'Zaszyfrowana wiadomość: {encrypted[0]} ... {encrypted[-1]} - {len(encrypted)} elementów')
    decrypted = decrypt_message(encrypted, private_key)
    print(f'Odszyfrowana wiadomość: {decrypted}')
    

if __name__ == '__main__':
    main()
