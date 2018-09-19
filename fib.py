import timeit
import cProfile

class memoize:
    
  def __init__(self, function):
    self.function = function
    self.store = {}

  def __call__(self, *args):
    key = (args)
    if not key in self.store:
      self.store[key] = self.function(*args)
    return self.store[key]

def fib(n):

    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

@memoize
def fib2(n):

    if n == 0: return 0
    if n == 1: return 1
    return fib2(n-2) + fib2(n-1)


def fib3(n):

    if n < 2:
        return n
    return fib3(n-2) + fib3(n-1)

@memoize
def fib4(n):

    if n < 2:
        return n
    return fib4(n-2) + fib4(n-1)

x = 46
'''
cProfile.run("fib(%d)" % x)
cProfile.run("fib2(%d)" % x)
cProfile.run("fib3(%d)" % x)
cProfile.run("fib4(%d)" % x)
'''
timer_start = timeit.default_timer()
fib(x)
timer_end = timeit.default_timer()
print(f'{timer_end - timer_start:.10f}')
timer_start = timeit.default_timer()
fib2(x)
timer_end = timeit.default_timer()
print(f'{timer_end - timer_start:.10f}')
timer_start = timeit.default_timer()
fib3(x)
timer_end = timeit.default_timer()
print(f'{timer_end - timer_start:.10f}')
timer_start = timeit.default_timer()
fib4(x)
timer_end = timeit.default_timer()
print(f'{timer_end - timer_start:.10f}')
