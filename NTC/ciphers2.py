def vernam(pt, key):
    result = ""

    for i in range(len(pt)):
        # result += chr(ord(pt[i]) ^ ord(key[i]))
        result += str(int(pt[i]) ^ int(key[i]))
    return result


pt = input("Enter plaintext: ")
key = input("Enter key: ")

if len(pt) == len(key):
    ct = vernam(pt, key)
    print("Encrypted:", ct)
    print("Decrypted:", vernam(ct, key))
else:
    print("Plaintext and key must have same length")

def vigerene(pt, k, mode):
    res = ""

    for i in range(len(pt)):
        a = ord(pt[i])-65
        b = ord(k[i%len(k)])-65
        if mode == 'e': 
            c = (a+b)%26
        else:
            c = (a-b)%26
        
        res += chr((c+65))

    return res

pt = input("enter pt")
k = input("enter k")
ct = vigerene(pt,k, 'e')
print(ct)
print(vigerene(ct,k, 'd'))

def railfence(pt, n):
    rails = [""] * n
    r = 0
    direction = 1

    for ch in pt:
        rails[r] += ch

        if r == 0:
            direction = 1
        elif r == n-1:
            direction = -1

        r+=direction

    return ''.join(rails)


pt = input("Enter plaintext: ")
n = int(input("Enter number of rails: "))

print("Encrypted:", railfence(pt, n))