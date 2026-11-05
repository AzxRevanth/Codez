def add_cayley(n):
    for i in range(n):
        for j in range(n):
            print((i+j)% n, end="")
        print("")

def mul_cayley(n):
    for i in range(n):
        for j in range(n):
            print((i*j)% n, end="")
        print(" ")

add_cayley(4)
print()
mul_cayley(4)