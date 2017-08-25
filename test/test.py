import socket
import time
import argparse
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

        # if args.port != 0:
        #     self.port = 80
        #     std.write("Port: "+str(self.port))
        #     #self.config.set("Setting", "port", "{}".format(self.port))
        #
        #
        # if args.dell:
        #     self.host = []
        #     std.write(', '.join(self.host)+'\n\n')
        #     #self.config.set("Setting", "list", "{}".format(",".join(self.host)))
        #
        #
        # if args.rmip != 'rmip':
        #
        #     self.host.remove(args.rmip)
        #     std.write(', '.join(self.host))
        #     #self.config.set("Setting", "list", "{}".format(','.join(self.host)))
        #
        #
        # if args.addlist != 'd':
        #     if args.addlist != '' and len(args.addlist) >= 1:
        #         for i in args.addlist:
        #             self.host.append(i)
        #
        #         std.write(', '.join(self.host))
        #         std.write("\n"+str(len(self.host)))
        #         self.config.set("Setting", "list", "{}".format(",".join(self.host)))
        #     else:
        #         std.write("it cant be EMPTY")
        #
        # if args.addip != None:
        #     self.host.append(args.addip)
        #     std.write(', '.join(self.host))
        #     self.config.set("Setting", "list", "{}".format(",".join(self.host)))
        #
        # with open('vars.ini', 'w') as f:
        #     self.config.write(f)

        for i in self.host:
            try:
                self.RUN(i)
            except:
                std.write("\nEEERROOR")



    def get_arges(self):
        pass
            # parse = argparse.ArgumentParser()
            #
            # parse.add_argument('--addlist', nargs='+', default='d',
            #                    help='add a new list of ips')
            #
            # parse.add_argument('--addip', type=str, default=None,
            #                    help='add an ip')
            #
            # parse.add_argument('--rmip', type=str, default='rmip',
            #                    help='remove an ip')
            #
            # parse.add_argument('--dell', type=bool, default=False,
            #                    help='delete the ip list')
            #
            # parse.add_argument('--port', type=int, default=80,
            #                    help="change the port")
            #
            # args = parse.parse_args()
            # return args


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
            std.write('\nit took {}s to respond\n'.format(round(end-start, 3)))

        except socket.gaierror:
            std.write('\n{} IS NOT WORKING :('.format(i))


check_online()
