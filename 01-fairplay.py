from sys import argv


def main(text, secret: str, decrypt=False, direction="v"):
    text = [x for x in text.lower()]
    key = build_key(secret)
    for index, i in enumerate(key):
        if (index % 5) < 4:
            print(i, end=' ')
        else:
            print(i)
    print(''.join(text))
    shifted = encrypt_text(text, key, direction)
    print(''.join(shifted))
    returned = decrypt_text(shifted, key, direction)
    print(''.join(returned))
    exit(0)


def encrypt_text(text_list: list, key: list, direction="v"):
    i = -2
    j = 1
    while True:
        a = None
        b = None
        i += 1+j
        j = 1
        if i >= len(text_list):
            break
        while a is None:
            temp = text_list[i]
            if temp.isalpha():
                a = key.index(temp)
                break
            i += 1
        while b is None:
            try:
                temp = text_list[i+j]
            except IndexError:
                if temp == 'x':
                    b = key.index('y')
                else:
                    b = key.index('x')
                text_list.insert(i + j, ' ')
                break
            if temp.isalpha():
                if temp == text_list[i]:
                    if temp == 'x':
                        b = key.index('y')
                    else:
                        b = key.index('x')
                    text_list.insert(i + j, ' ')
                    break
                b = key.index(temp)
                break
            j += 1
        if a//5 == b//5:
            a = ((a // 5) * 5) + ((a + 1) % 5)
            b = ((b // 5) * 5) + ((b + 1) % 5)
        if a % 5 == b % 5:
            a = (a + 5) % 25
            b = (b + 5) % 25
        else:
            if direction == 'v':
                a, b = (a % 5) + ((b // 5) * 5), (b % 5) + ((a // 5) * 5)
            if direction == 'h':
                a, b = ((a // 5) * 5) + (b % 5), ((b // 5) * 5) + (a % 5)
        text_list[i] = key[a]
        text_list[i + j] = key[b]
    return text_list


def decrypt_text(text_list: list, key: list, direction="v"):
    i = -2
    j = 1
    while i < len(text_list)-2:
        a = None
        b = None
        i += 1+j
        j = 1
        while a is None:
            temp = text_list[i]
            if temp.isalpha():
                a = key.index(temp)
                break
            i += 1
        while b is None:
            temp = text_list[i+j]
            if temp.isalpha():
                b = key.index(temp)
                break
            j += 1
        if a//5 == b//5:
            a = ((a // 5) * 5) + ((a - 1) % 5)
            b = ((b // 5) * 5) + ((b - 1) % 5)
        if a % 5 == b % 5:
            a = (a - 5) % 25
            b = (b - 5) % 25
        else:
            if direction == 'v':
                a, b = (a % 5) + ((b // 5) * 5), (b % 5) + ((a // 5) * 5)
            if direction == 'h':
                a, b = ((a // 5) * 5) + (b % 5), ((b // 5) * 5) + (a % 5)
        text_list[i] = key[a]
        text_list[i + j] = key[b]
    return text_list


def build_key(secret: str):
    secret = secret.replace('j', 'i')
    alphabet = list('abcdefghiklmnopqrstuvwxyz')
    parsed_secret = []
    for letter in secret:
        if letter not in parsed_secret:
            parsed_secret.append(letter)
            alphabet.remove(letter)
    arr = parsed_secret+alphabet
    return arr


if __name__ == "__main__":
    if len(argv) == 5:
        argv[3] = True if argv[3].lower() == "d" else False
        main(argv[1], argv[2], argv[3], argv[4])
    elif len(argv) == 4:
        argv[3] = True if argv[3].lower() == "d" else False
        main(argv[1], argv[2], argv[3])
    elif len(argv) == 3:
        main(argv[1], argv[2])
    else:
        print("Argument error")
        print("Usage: {argv[0]} <message> <secret> [decrypt? T/F] [direction v/h]")
        exit(-1)
