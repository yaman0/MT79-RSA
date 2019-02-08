import Tools


def chiffrement(m, n, d):
    return Tools.modpow(m, d, n)


def dechiffrement(m, n, c):
    return Tools.modpow(m, c, n)


def findPrivateKey(n, c):
    divisors = [d for d in xrange(2, n / 2) if n % d == 0]
    p = divisors[0]
    q = n / p
    d = Tools.inverseModulaire(c, (p - 1) * (q - 1))
    return d
