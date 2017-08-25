import socket

host = 'iocl.com'
port = 80
def make_connection(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host, port)
    return s

def RUN(request, host, port):
    s = make_connection(host=host, port=port)
    s.send(request.encode())
    output = s.recv(4000)
    print(output.decode())