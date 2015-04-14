#!/usr/bin/env python

import threading
import time

from flask import request
from flask import Flask
app = Flask(__name__)

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
    d.stop()
    shutdown_server()
    return "shutting down."


## ------------------------------------------------------------

class Daemon(threading.Thread):

    def __init__(self):
        super(Daemon, self).__init__()
        self.shutdown = False

    def stop(self):
        self.shutdown = True
        print("shutdown SET")
        
    def run(self):
        while not self.shutdown:
            print("tick")
            time.sleep(2)
        print("shutdown has arrived.")


if __name__ == "__main__":
    d = Daemon()
    d.start()
    app.run(host='0.0.0.0')
