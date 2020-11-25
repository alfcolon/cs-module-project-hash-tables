import random
import math
import time

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

xy_cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    global xy_cache
    key = (x, y)
    if key not in xy_cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        xy_cache[key] = v
    return xy_cache[key]

# Do not modify below this line!
start = time.time()
for i in range(10000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    slowfun_too_slow(x, y)
#    print(f'{i}: {x},{y}: {slowfun(x, y)}')
end = time.time()
print(end - start)
