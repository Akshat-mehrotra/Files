import socket
import time
from sys import stdout as std
import configparser as cp


class check_online():
    def __init__(self):

        self.host = []

        self.config2 = cp.ConfigParser()
        self.config2.read('vars.ini')

        try:

            self.host = self.config2.get("Setting", "list").split(',')
            std.write('it was able to get it')

        except:
            std.write("the list is empty\n\n")

            self.host = []

        self.port = int(self.config2.get('Setting', 'port'))



        for i in self.host:
            try:
                self.RUN(i)
            except:
                std.write("\nEEERROOR")


    def make_connection(self, i):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((i, self.port))
        return s

    def RUN(self, i):
        try:
            start = time.time()
            self.make_connection(i)
            end = time.time()

            std.write('\n{} IS WORKING'.format(i))
            std.write('\nit took {}s to respond\n'.format(round(end - start, 3)))
            with open('C:\\Users\\Akshat\\Desktop\\log.txt', 'a') as f:

                
        except socket.gaierror:
            std.write('\n{} IS NOT WORKING :('.format(i))
            with open('C:\\Users\\Akshat\\Desktop\\log.txt', 'a') as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S: ", time.gmtime())+'\n{} IS NOT WORKING\n\n'.format(i))


check_online()
