def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return gcd, x, y

def diphontine(a,b,c):
    gcd, x, y = extended_gcd(abs(a), abs(b))

    if c%gcd != 0:
        print("No sol")
        return 

    x = x*(c//gcd)
    y = y*(c//gcd)

    if a < 0:
        x = -x
    if b < 0:
        y = -y

    return x,y

a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))
x,y = diphontine(a,b,c)

print(x)
print(y)
