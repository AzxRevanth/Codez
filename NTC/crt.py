def crt(a,m):
    M = 1

    for num in m:
        M*=num

    x = 0
    for i in range(len(m)):
        Mi = M // m[i]
        Mi_inv = pow(Mi, -1, m[i])
        x+= a[i] * Mi_inv * m[i]

    res = x % M

    return res

a = [2, 3, 2]
m = [3, 5, 7]

print("x =", crt(a, m))