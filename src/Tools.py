def modpow(n, pow, mod):
    if pow == 0:
        return 1
    elif pow % 2 == 0:
        return (modpow(n, pow / 2, mod) * modpow(n, pow / 2, mod)) % mod
    else:
        return (n * modpow(n, pow / 2, mod) * modpow(n, pow / 2, mod)) % mod
