def xor(a,b):
    res = ""
    for i in range(len(a)):
        res += str(int(a[i]) ^ int(b[i]))

    return res

def fiestal(left, right, key):
    # left = pt[:len(pt)//2]
    # right = pt[len(pt)//2:]
    new_left = right
    new_right = xor(left, xor(right, key))
    return new_left, new_right

def des(pt, key):
    left = pt[:len(pt)//2]
    right = pt[len(pt)//2:]

    for i in range(16):
        print(f"{i} Iteration ")
        left, right = fiestal(left, right, key)

    return left+right


pt = input("Enter binary pt ")
key = input("Enter key ")
res = des(pt, key)
print(res)
# print(left)
# print(right)

