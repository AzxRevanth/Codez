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

def last(a,p):
    ph = phi(10)
    exp = p % ph
    return pow(a,exp)%10

def lastlast(a,p):
    ph = phi(100)
    exp = p % ph
    return pow(a,exp)%100

def lastlastlast(a,p):
    ph = phi(1000)
    exp = p % ph
    return pow(a,exp)%1000


print(last(17,22))
print(lastlast(17,22))
print(lastlastlast(17,22))