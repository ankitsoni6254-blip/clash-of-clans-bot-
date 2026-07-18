import time
import random

def sleep(minimum, maximum=None):
    if maximum is None:
        time.sleep(minimum)
    else:
        time.sleep(random.uniform(minimum, maximum))
