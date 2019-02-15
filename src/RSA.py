import math

import MathTools


def chiffrement(m, n, c):
    """
    encrypt a number m with a public key (n,c)
    :param int m: number to crypt
    :param int n: n from public key
    :param int c: c from public key
    :return int : m encrypt
    """
    return MathTools.modpow(m, c, n)


def dechiffrement(m, n, d):
    """
    decrypt a number m with a private key (n,d)
    :param int m: number to decrypt
    :param int n: n from private key
    :param int d: d from private key
    :return int: decrypt
    """
    return MathTools.modpow(m, d, n)


def findPrivateKey(n, c):
    """
    find the private key from a public key
    :param int n: n from public key
    :param int c: d from public key
    :return int: d from public key
    """
    # Generate divisors from 2 to sqrt(n)
    divisors = [d for d in xrange(2, int(math.sqrt(n))) if n % d == 0]
    p = divisors[0]
    q = n / p
    d = MathTools.inverseModulaire(c, (p - 1) * (q - 1))
    return d
