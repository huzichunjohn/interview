#/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from contextlib import contextmanager
import random

@contextmanager
def print_execute_time(task_name):
    start = time.time()
    try:
        yield
    finally:
        print task_name, "took", time.time() - start, "seconds."

with print_execute_time("range"):
    for i in range(10):
        print i
        # time.sleep(random.randint(1,3))
