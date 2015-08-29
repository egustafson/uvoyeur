"""uVoyeur Application Bus"""


class PublishFailures(Exception):

    delimiter = '\n'

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self._exceptions = list()

    def capture_exception(self):
        self._exceptions.append(sys.exc_info()[1])

    def get_instances(self):
        return self._exceptions[:]

    def __str__(self):
        exception_strings = map(repr, self.get_instances())
        return self.delimiter.join(exception_strings)

    __repr__ = __str__

    def __bool__(self):
        return bool(self._exceptions)

    __nonzero__ = __bool__



class Bus(object):

    def __init__(self):
        self.listeners = dict(
            [(channel, set()) for channel 
             in ('main')])
        print("Bus() initialized.")


    def subscribe(self, channel, callback):
        if channel not in self.listeners:
            self.listeners[channel] = set()
        self.listeners[channel].add(callback)


    def unsubscribe(self, channel, callback):
        listeners = self.listeners.get(channel)
        if listeners and callback in listeners:
            listeners.discard(callback)


    def publish(self, channel, *args, **kwargs):
        """Return the output of all subscribers in an array."""
        if channel not in self.listeners:
            return []

        exc = PublishFailures()
        output = []

        listeners = self.listeners.get(channel)
        for listener in listeners:
            try:
                output.append(listener(*args, **kwargs))
            except KeyboardInterrupt:
                raise
            except SystemExit:
                # If there were previous (non SystemExit) errors, make sure exit code in non-zero
                e = sys.exc_info()[1]
                if exc and e.code == 0:
                    e.code = 1
                # propigate SystemExit
                raise
            except:
                exc.capture_exception()
                # and continue publishing

        if exc:
            raise exc
        return output



## Local Variables:
## mode: python
## End:
