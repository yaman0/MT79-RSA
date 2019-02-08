import math


def modpow(n, pow, mod):
    result = 1
    while pow > 0:
        if (pow & 1) > 0:
            result = (result * n) % mod
        pow >>= 1
        n = (n ** 2) % mod
    return result


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def euclideDiv(a, b):
    r = a % b
    q = (a - r) / b
    return q, r


def euclidExtend(a, b):
    r = 1
    u, v = 1, 0
    u_, v_ = 0, 1
    _u, _v, _r = 0, 0, 0  # Temp vars
    while b != 0:
        q, r = euclideDiv(a, b)  # divide
        _r, _u, _v = a, u, v  # update temp
        a, u, v = b, u_, v_  # shift
        b, u_, v_ = r, _u - q * u_, _v - q * v_  # computed
    return a, u, v


def inverseModulaire(a, n):
    pgcd, u, v = euclidExtend(a, n)
    if not pgcd == 1:
        raise ValueError('PGCD != 1')
    return u % n


def generationExposant(p, q):
    c, d = 2, 0
    phi = (p - 1) * (q - 1)
    while not gcd(phi, c) == 1:
        c += 1
    d = inverseModulaire(c, phi)
    return c, d


def primeFactors(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            result.append(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        result.append(n)
    return result
