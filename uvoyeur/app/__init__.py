""" Client (App) library for uVoyeur.

More lengthy description.
"""
#
# Author: Eric Gustafson (29 Aug 2015) <eg-git@elfwerks.org>
#
# ############################################################

import uvoyeur.app.Agent


_agent = None

def get_agent(**kwargs):
    if _agent:
        return _agent
    ## otherwise initialize the agent
    _agent = uvoyeur.app.Agent.init_agent(kwargs)
    return _agent


def hook__logs(**kwargs):
    #
    # Do what's needed to hook into the native
    # logging system (Python logs in this case)
    #
    # hook into == capture all logs and feed
    #  upstream to Voyeur agents.
    #


## Local Variables:
## mode: python
## End:
