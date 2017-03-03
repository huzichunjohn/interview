#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds):
    def decorator(func):
        def handle_timeout(signum, frame):
            raise TimeoutError("Timeout.")

        def wrapper(*args, **kwargs):
            old_handler = signal.signal(signal.SIGALRM, handle_timeout)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old_handler)
                signal.alarm(0)

            return result

        return wrapper

    return decorator

@timeout(5)
def foo():
    for i in range(1, 10):
        time.sleep(1)
        print "%d seconds have passed" % i

if __name__ == "__main__":
    foo()
