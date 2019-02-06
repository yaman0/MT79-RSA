def modpow(n, pow, mod):
    if pow == 0:
        return 1
    elif pow % 2 == 0:
        return (modpow(n, pow / 2, mod) * modpow(n, pow / 2, mod)) % mod
    else:
        return (n * modpow(n, pow / 2, mod) * modpow(n, pow / 2, mod)) % mod


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
