"""uVoyeur daemon."""

from uvoyeur.daemon.bus import Bus

vbus = Bus()

## Start the daemon - called with initialization parameters.
##  - see run() for direct CLI execution.
##
def start(args=None):
    import uvoyeur.daemon.http_proto as http_srv
    import uvoyeur.daemon.mcast_proto as mcast

    mcast.McastListener(vbus).subscribe()

    h = http_srv.HttpServer(vbus)
    h.subscribe()

    vbus.publish('start')
    h.block()
    vbus.publish('stop')


## Run the daemon (from the CLI).
##
def run():
    import argparse

    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    start(args)
    print('done.')
    

## Local Variables:
## mode: python
## End:
