import socket

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


s = socket.socket()
s.bind('localhost', 1234)
s.listen()
conn, _ = s.accept()
a,b = map(int, conn.recv(1024).decode().split())

g = gcd(a,b)

conn.send(str(a).encode())

conn.close()
s.close()
