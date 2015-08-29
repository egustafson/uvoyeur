"""PROTOTYPE - HTTP server (cherrypy)

REPLACE with full HTTP server in time.
"""

import cherrypy

class VoyeurRootHttp(object):

    @cherrypy.expose
    def index(self):
        return "uVoyeur - index"

    @cherrypy.expose
    def shutdown(self):
        return "uVoyeur - shuttingdown...  (not working yet)"



class HttpServer(object):

    def __init__(self, bus):
        self.bus = bus

    def subscribe(self):
        self.bus.subscribe('start', self.start)
        self.bus.subscribe('stop', self.stop)

    def block(self):
        print("uVoyeur HTTPServer - block")
        cherrypy.engine.block()
        print("uVoyeur HTTPServer - block -- finished.")

    def start(self):
        cherrypy.config.update({'server.socket_host': '0.0.0.0'})
        cherrypy.tree.mount(VoyeurRootHttp(), '/')
        cherrypy.engine.start()
        print("uVoyeur HTTPServer - start")

    def stop(self):
        print("uVoyeur HTTPServer - stop")



## Local Variables:
## mode: python
## End:
