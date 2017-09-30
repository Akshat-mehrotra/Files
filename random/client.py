import socket

s = socket.socket()
s.connnect(("It's ye boi", 1974))
with open('movie.mov', 'rb') as f:
    l = f.read(4000)
    while l:
        s.send(l)
        l = f.read(4000)
s.close()         
