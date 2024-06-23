import time

DEFAULT_FMT = '[{elapsed:0.8f}s]'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        t0 = time.perf_counter()
