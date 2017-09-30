import socket

s = socket.socket()
s.bind(('', 8080))
s.listen(10)

while True:
    sc, add = s.accept()
    print(add)
    with open('image.jpg', 'wb') as f:
        while True:
            l = sc.recv(4000)
            while l:
                f.write(l)
                l = sc.recv(4000)
            break
    break    
    sc.close()
    print('done')
s.close()
print('done')
