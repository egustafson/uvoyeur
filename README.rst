uVoyeur - Testbed for the Voyeur monitoring framework
=====================================================

A Python based skeleton that will be used to prototype all aspects of
the (final) Voyeur tools.

What is Voyeur?   An integration and gentle reshaping of today's
monitoring tools and concepts with the end goal of being able to
meaningfully installing "monitoring" on a node by simply stating
something to the effect of `apt-get install voyeur`.

-- Basic monitoring should be simple; advanced monitoring should be
configurable.

----

Details of this repository, installation, configuration, operation:
TBD


Testing
-------

Designed to use Nose2 (https://nose2.readthedocs.org/en/latest/),
built on top of Python's unittest framework.

   > nose2


Development
-----------

Install locally using:

   > python3 setup.py develop --user

See https://setuptools.pypa.io/en/latest/setuptools.html#automatic-script-creation

This package uses Setuptools and prefers Python 3.


.. Local Variables:
.. mode: rst
.. End:
