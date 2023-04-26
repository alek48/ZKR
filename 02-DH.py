from sympy import randprime
from random import randrange, choice
from math import sqrt

MIN_VAL = 10**3
MAX_VAL = 10**4


def findPrimefactors(n):
    s = set()
    while (n % 2 == 0):
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n))+1, 2):
        while (n % i == 0):
            s.add(i)
            n = n // i
    if (n > 2):
        s.add(n)
    return s


def findPrimitives(n):
    phi = n - 1
    primitives = []
    s = findPrimefactors(phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if (pow(r, phi // it, n) == 1):
                flag = True
                break
        if not flag:
            primitives.append(r)
    return primitives


class DH:

    def __str__(self):
        return "|".join([str(x) for x in [self.n, self.g, self.private_key, self.public_key, self.k]])

    @classmethod
    def simulate_DH_session_key(self, verbose=False):
        client1 = DH()
        client2 = DH()
        DH.set_A_and_B(client1, client2, MIN_VAL, MAX_VAL)
        client1.calculate_keys(MIN_VAL, MAX_VAL)
        client2.calculate_keys(MIN_VAL, MAX_VAL)
        DH.exchange_public_keys(client1, client2)
        client1.calculate_session_key()
        client2.calculate_session_key()
        if verbose:
            headers = ["n", "g", "klucz prywatny", "klucz publiczny", "klucz sesji"]
            for properties in zip(headers, str(client1).split("|"), str(client2).split("|")):
                [print(str(elem)[:min(len(str(elem)), 15)].rjust(17), end="") for elem in properties]
                print()

    @classmethod
    def set_A_and_B(self, c1, c2, lower_bound, upper_bound):
        n = randprime(lower_bound, upper_bound)
        g = findPrimitives(n)
        c1.n = c2.n = n
        c1.g = c2.g = choice(g)

    @classmethod
    def exchange_public_keys(self, c1, c2):
        c1.other_key = c2.public_key
        c2.other_key = c1.public_key
        return

    def calculate_keys(self, lower_bound, upper_bound):
        self.private_key = randrange(lower_bound, upper_bound)
        self.public_key = pow(self.g, self.private_key, self.n)

    def calculate_session_key(self):
        self.k = pow(self.other_key, self.private_key, self.n)


def main():
    DH.simulate_DH_session_key(True)


if __name__ == "__main__":
    main()
