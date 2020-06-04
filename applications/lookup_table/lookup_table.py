import math
import random
from time import sleep


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


mod_result = {}


def slowfun(x, y, mod_result):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) not in mod_result:
        mod_result[(x, y)] = slowfun_too_slow(x, y)
        print(f"Added {len(mod_result)}/36 results so far")
        sleep(0.3)

    return mod_result[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y, mod_result)}')
