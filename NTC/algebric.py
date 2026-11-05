# def cayley(s,n,op):
#     T = []

#     for a in s:
#         row = []
#         for b in s: 
#             if op = '+':
#                 row.append((a+b)%n)
#             elif op == '*':
#                 row.append((a*b) % n)
#         T.append(row)

#     return T

def semi_group(s,n,op): #closure and associative
    #closure
    for a in s:
        for b in s:
            if op == '+':
                if (a+b)%n not in s:
                    return False
            elif op == '*':
                if (a*b)%n not in s:
                    return False

    for a in s:
        for b in s:
            for c in s:
                if op == '+':
                    if ((a+b)%n+c)%n != (a+(b+c)%n)%n:
                        return False
                elif op == '*':
                    if ((a*b)%n*c)%n != (a*(b*c)%n)%n:
                        return False

    return True

def commutative(s,n,op):
    for a in s:
        for b in s: 
            if op == '+':
                if (a+b)%n != (b+a)%n:
                    return False
            elif op == '*':
                if (a*b)%n != (b*a)%n:
                    return False

    return True

def identity(s,n,op):
    for e in s:
        valid = True
        for a in s:
            if op == '+':
                if (a+e)%n != a or (e+a)%n != a:
                    valid = False
            elif op == '*':
                if (a*e)%n != a or (e*a)%n != a:
                    valid = False
        if valid:
            return e
    return None

def inverse(s,n,op):
    if identity(s,n,op) == None:
        return False

    e = identity(s,n,op)

    for a in s:
        found = False
        for b in s:
            if op == '+':
                if (a+b)%n == e:
                    found = True
            elif op == '*':
                if (a*b)%n == e:
                    found = True
        if not found:
            return False
    return True 

def group(s,n,op):
    if not semi_group(s,n,op):
        return False

    if identity(s,n,op) is None or not inverse(s,n,op):
        return False
    
    return True

def abelian_group(s,n,op):
    if not group(s,n,op):
        return False

    if not commutative(s,n,op):
        return False

    return True

def distributive(s, n, op1, op2):
    for a in s:
        for b in s:
            for c in s:
                if op1 == '+' and op2 == '*':
                    if (a*(b+c))%n != ((a*b)%n+(a*c)%n)%n:
                        return False

                elif op1 == '*' and op2 == '+':
                    if ((a+b)%n*c)%n != ((a*c)%n+(b*c)%n)%n:
                        return False

    return True

def ring(s,n,op1,op2):
    if not abelian_group(s,n,op1):
        return False
    if not semi_group(s,n,op2):
        return False
    if not distributive(s,n,op1,op2):
        return False
    return True

def commutative_ring(s,n,op1,op2):
    if not ring(s,n,op1,op2):
        return False

    if not commutative(s,n,op2):
        return False

    return True

def field(s,n,op1,op2):
    if not ring(s,n,op1,op2):
        return False

    if not commutative(s,n,op2):
        return False

    zero = identity(s,n,op1)
    one = identity(s,n,op2)

    if zero == one:
        return False

    for a in s:
        if a != zero:
            found = False
            for b in s:
                if (a*b)%n == one:
                    found = True
                    break
            if not found:
                return False

    return True

def prime_field(s,n,op1,op2):
    if field(s,n,op1,op2) and len(s) > 1:
        for i in range(2,len(s)):
            if len(s)%i == 0:
                return False
        return True
    return False


def galois_field(s,n,op1,op2):
    if not field(s,n,op1,op2):
        return False

    p = len(s)

    for i in range(2,p):
        if p%i == 0:
            while p%i == 0:
                p //= i

            if p == 1:
                return True

    return p == 1

s = [0, 1, 2, 3, 4]
n = 5

op1 = '+'
op2 = '*'

print("Semigroup (+):", semi_group(s,n,op1))
print("Semigroup (*):", semi_group(s,n,op2))

print("Commutative (+):", commutative(s,n,op1))
print("Commutative (*):", commutative(s,n,op2))

print("Identity (+):", identity(s,n,op1))
print("Identity (*):", identity(s,n,op2))

print("Inverse (+):", inverse(s,n,op1))
print("Inverse (*):", inverse(s,n,op2))

print("Group (+):", group(s,n,op1))
print("Abelian Group (+):", abelian_group(s,n,op1))

print("Distributive:", distributive(s,n,op1,op2))

print("Ring:", ring(s,n,op1,op2))
print("Commutative Ring:", commutative_ring(s,n,op1,op2))
print("Field:", field(s,n,op1,op2))

print("Prime Field:", prime_field(s,n,op1,op2))
print("Galois Field:", galois_field(s,n,op1,op2))