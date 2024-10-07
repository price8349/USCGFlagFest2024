import gmpy2
gmpy2.get_context().precision = 4096

from binascii import unhexlify
from functools import reduce
from gmpy2 import root

# Håstad's Broadcast Attack
# https://id0-rsa.pub/problem/11/

# Resources
# https://en.wikipedia.org/wiki/Coppersmith%27s_Attack
# https://github.com/sigh/Python-Math/blob/master/ntheory.py

EXPONENT = 5

ciphertexts = []
modulus = []

x = open("message(3).txt", "r")
for i in x:
    if ", " in i:
        z = i.split(", ")
        ciphertexts.append(int(z[0]))
        modulus.append(int(z[2]))

def chinese_remainder_theorem(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m

    # Make sure we return the canonical solution.
    return result % N


def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return (lastx, lasty, a)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_value(filename):
    with open(filename) as f:
        value = f.readline()
    return int(value, 16)

if __name__ == '__main__':
    C1 = ciphertexts[0]
    C2 = ciphertexts[1]
    C3 = ciphertexts[2]
    C4 = ciphertexts[3]
    C5 = ciphertexts[4]

    N1 = modulus[0]
    N2 = modulus[1]
    N3 = modulus[2]
    N4 = modulus[3]
    N5 = modulus[4]
    C = chinese_remainder_theorem([(C1, N1), (C2, N2), (C3, N3), (C4, N4), (C5, N5)])
    M = int(root(C, 5))

    M = hex(M)[2:]
    print(unhexlify(M))
