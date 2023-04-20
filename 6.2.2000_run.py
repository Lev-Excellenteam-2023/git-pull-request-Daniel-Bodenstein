import time

def timer(f, *params):
    start = time.time()
    f(params)
    end = time.time()
    print (start-end)