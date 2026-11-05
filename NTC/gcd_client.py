import socket

s = socket.socket()
s.connect(('localhost', 1234))

a = input("Enter first number: ")
b = input("Enter second number: ")

s.send((a + " " + b).encode())

print("GCD =", s.recv(1024).decode())

s.close()