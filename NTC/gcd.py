def highschool_gcd(a,b):
    res = 1
    limit = min(a,b)

    for i in range(1, limit+1):
        if a%i == 0 and b%i == 0:
            res=i
    return res

def euclidean_gcd(a,b):
    if b == 0:
        return a
    return euclidean_gcd(b,a%b)

def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return gcd, x, y

a = int(input("Enter a "))
b = int(input("Enter b "))

g1 = highschool_gcd(a,b)
g2 = euclidean_gcd(a,b)
g3, x, y = extended_gcd(a,b)

print(g1)
print(g2)
print(g3)