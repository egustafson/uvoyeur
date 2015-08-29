""" Client (App) Agent singleton

More description - TBD
"""
#
#  Author:  Eric Gustafson <eg-git@elfwerks.org> (29 Aug 2015)
#
# ############################################################

# import statement


def init_agent(**kwargs):
    # opportunity for pre/post hooks.
    return Agent(**kwargs)


class Agent:
    
    def __init__(self, **kwargs):
        None



## Local Variables:
## mode: python
## End:
