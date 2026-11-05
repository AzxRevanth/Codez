def gcd(a,b):
    if b == 0: 
        return a,1,0

    g, x1, y1 = gcd(b, a%b)
    x = y1
    y = x1-(a//b)*y1

    return g, x, y

a = int(input("Enter number: "))
b = int(input("Enter modulus: "))

g, x, y = gcd(a,b)

if g == 1:
    print("Inverse", x % b)
else:
    print("No")