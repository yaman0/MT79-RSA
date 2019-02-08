import Tools

def chiffrement(m, n, c):
    return Tools.modpow(m,c,n)

def dechiffrement(m, n, d):
    return Tools.modpow(m,d,n)
