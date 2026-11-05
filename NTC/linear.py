def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def linear_cong(a,b,n):
    # ax = b mod n
    g = gcd(a,n)

    if b % g != 0:
        print("No Sol")
        return 
    a = a // g
    b = b // g
    n = n // g

    inv = pow(a, -1, n)
    x = (b * inv) % n

    return x

res = linear_cong(4,8,12)
print(res)