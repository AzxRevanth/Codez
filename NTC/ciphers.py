import numpy as np
def ceaser(pt, k):
    ct = ""
    for ch in pt:
        ct+=chr(ord(ch)+k)
    return ct


print(ceaser("Hello", 3))

def playfair(pt, key, mode):
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key = key.upper().replace('J', 'I')
    k = ""
    for ch in key + alphabets:
        if ch not in k:
            k += ch

    table = [list(k[i:i+5]) for i in range(0,25,5)]

    pt = pt.upper().replace('J', 'I').replace(" ", "")
    new = ""

    if mode == 'e':
        i = 0
        while i < len(pt):
            a = pt[i]
            if i+1 == len(pt):
                b = 'X'
            elif pt[i+1] == pt[i]:
                b = 'X'
            else:
                b = pt[i+1]
                i += 1
            new += a+b
            i += 1
    else:
        new = pt

    results = ""

    for i in range(0,len(new),2):
        a = new[i]
        b = new[i+1]

        for r in range(5):
            for c in range(5):
                if table[r][c] == a:
                    r1,c1 = r,c
                if table[r][c] == b:
                    r2,c2 = r,c

        if r1 == r2:
            results += table[r1][(c1+(1 if mode == 'e' else -1))%5]
            results += table[r2][(c2+(1 if mode == 'e' else -1))%5]

        elif c1 == c2:
            results += table[(r1+(1 if mode == 'e' else -1))%5][c1]
            results += table[(r2+(1 if mode == 'e' else -1))%5][c2]

        else:
            results += table[r1][c2]
            results += table[r2][c1]

    return results


# key = input("Enter key: ")
# text = input("Enter message: ")

# print("Encrypted:", playfair(text, key, 'e'))
# print("Decrypted:", playfair(playfair(text, key, 'e'), key, 'd'))

def hill(pt, key):
    if len(pt)%2 != 0:
        pt+='X'

    res = ""

    for i in range(0, len(pt), 2):
        a = ord(pt[i])-65
        b = ord(pt[i+1])-65

        x = (key[0][0] * a)+(key[0][1]*b)%26
        y = (key[1][0] * a)+(key[1][1]*b)%26
        # out = key @ np.array([a,b]) 
        # x = out[0] % 26
        # y = out[1] % 26


        res += ((chr(x+65))+(chr(y+65)))

    return res


key = [[3, 3], [2, 5]]

pt = input("Enter plaintext: ")

print("Encrypted:", hill(pt, key))