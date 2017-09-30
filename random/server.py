import socket

s = socket.socket()
s.bind(("It's ye boi", 1974))
s.listen(10)

while True:
    sc, add = s.accept()

    with open('something.mp4', 'wb') as f:
        while True:
            l = sc.recv(4000)
            while l:
                f.write(l)
                l = sc.recv(4000)
    sc.close()

s.close()
print('done')
