#!/usr/bin/env python

import socket
import struct
import threading

from flask import request
from flask import Flask
app = Flask(__name__)

## Constants --------------------------------------------------
MCAST_GRP  = '224.1.1.1'
MCAST_PORT = 5007

## ------------------------------------------------------------
## Flask aspects
##

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with Werkzeug Server')
    func()

@app.route("/")
def index():
    return "index - tbd"

@app.route("/shutdown")
def sd():
    mcl.stop()
    shutdown_server()
    return "shutting down."

## ------------------------------------------------------------
## Mcast Listener Daemon
##

class McastListener(threading.Thread):

    def __init__(self):
        super(McastListener, self).__init__()
        self.shutdown = False

    def stop(self):
        self.shutdown = True
        print("shutdown SET")
        
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
                print("sock-tick")
        print("shutting down.")

################################################
## Main 
##

if __name__ == "__main__":
    mcl = McastListener()
    mcl.start()
    app.run(host='0.0.0.0')
