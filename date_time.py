import time


def local_time():
    current = time.localtime()
    current_time = time.strftime("%d/%m/%Y", current)
    return current_time





