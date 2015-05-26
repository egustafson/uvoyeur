"""PROTOTYPE - Multicast Listener

REPLACE with full Mcast Listener in time
"""

import socket
import struct
import threading

MCAST_GRP  = '224.1.1.1'
MCAST_PORT = 5007

class McastListener(threading.Thread):

    def __init__(self, bus):
        super(McastListener, self).__init__()
        self.setDaemon(True)
        self.bus = bus
        self.shutdown = False

    def subscribe(self):
        self.bus.subscribe('start', self.do_start)
        self.bus.subscribe('stop', self.stop)

    def do_start(self):
        print("McastListener - start")
        self.start()

    def stop(self):
        self.shutdown = True
        print("McastListener - shutdown")
        
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        sock.settimeout(1)
        while not self.shutdown:
            try:
                msg = sock.recv(10240)
                print("received: {0}".format(msg))
            except socket.timeout:
                #print("sock-tick")
                pass
        print("shutting down.")

