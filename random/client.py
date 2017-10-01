import socket

host = '122.12.2.32'
s = socket.socket()
s.connect((host, 8080))
with open('image.jpg', 'rb') as f:
    l = f.read(4000)
    while l:
        s.send(l)
        l = f.read(4000)
s.close()         
