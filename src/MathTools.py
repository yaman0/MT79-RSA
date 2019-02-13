import math


def modpow(n, pow, mod):
    """
    Calculate the modular power.
    Algorithm from https://fr.wikipedia.org/wiki/Exponentiation_modulaire
    :param int n: number
    :param int pow: power
    :param int mod: modular
    :return:
    """
    result = 1
    while pow > 0:
        if (pow & 1) > 0:
            result = (result * n) % mod
        pow >>= 1
        n = (n ** 2) % mod
    return result


def gcd(a, b):
    """
    Compute the gcd
    :param int a: number a
    :param int b: number b
    :return int: gcd
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def euclideDiv(a, b):
    """
    Euclide division between a and b
    :param int a: number a
    :param int b: number b
    :return int,int : quotient, remainder
    """
    r = a % b
    q = (a - r) / b
    return q, r


def euclidExtend(a, b):
    """
    Compute the Euclide extended
    Algorithm from https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
    :param int a: number a
    :param int b: number b
    :return: Euclide extended
    """
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
    """
    Compute modular inverse
    :param int a: number
    :param int n: modulo
    :return: modular inverse
    """
    gcd, u, v = euclidExtend(a, n)
    if not gcd == 1:
        raise ValueError('GCD != 1')
    return u % n


def generationExposant(p, q):
    """
    Generate c and d. c prime with (p-1)(q-1) and d % (p-1)(q-1) = 1
    :param int p: number p
    :param int q: number q
    :return int,int : c prime with (p-1)(q-1) and d % (p-1)(q-1) = 1
    """
    c, d = 2, 0
    phi = (p - 1) * (q - 1)
    while not gcd(phi, c) == 1:
        c += 1
    d = inverseModulaire(c, phi)
    return c, d


def primeFactors(n):
    """
    Find prime factor with n
    :param int n: a number
    :return list: list of prime factors
    """
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            result.append(i)
            n = n / i

    # number greater than 2
    if n > 2:
        result.append(n)
    return result
