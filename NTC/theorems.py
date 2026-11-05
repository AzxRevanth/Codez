def gcd(a,b):
    if b == 0: 
        return a 
    return gcd(b, a%b)

def phi(n):
    count = 0
    for i in range(1, n+1):
        if gcd(n, i) == 1:
            count+=1
    return count

def isprime(p):
    if p < 2:
        return False
    for i in range(2,p):
        if p%i==0:
            return False

    return True

def fermat(a,p,n):
    if not isprime(p):
        return False

    if gcd(a,p) != 1:
        return False

    if(pow(a,p-1)%n != 1):
        return False

    print(pow(a,p-1)%n)
    return True

def euler(a,n):
    p = phi(n)

    if gcd(a,n) != 1:
        return False

    if(pow(a,p)%n != 1):
        return False

    print(pow(a,p)%n)
    return True

print(fermat(2,5,5))  # True
print(euler(3,10))    # True