
import sys, psutil, multiprocessing
from multiprocessing import Pool
from multiprocessing import cpu_count
from psutil import virtual_memory
import time
from functools import partial

t = 0
newlist = []

def LoadMemory(percent, timetoload):
    currentMemory = virtual_memory().percent
    totalRAM = round(virtual_memory().total / (2 ** 30))
    print('Current utilized memory = ', currentMemory, "%")
    MemToFill_percent = percent
    t = timetoload
    while MemToFill_percent <= currentMemory:
        print('Already utilzed! ')
        return
    MemToFillMore = int(MemToFill_percent - currentMemory)
    new_list = [0] * int((10 ** 6 * 11) * totalRAM / 8) * int(MemToFillMore)
    print('After loading memory utilized=', virtual_memory().percent, "%")
    time.sleep(t)
    new_list.clear()
    print('After clearing memory utilized=', virtual_memory().percent, "%")


def f(x, load, t):
    print('load=', load)
    percent_cpu = load / 100  # Should ideally replace this with a smaller number e.g. 20
    timeout = time.time() + x
    while time.time() < timeout:
        start_time = time.process_time()
        while time.process_time() - start_time < percent_cpu:
            x = 1 * 1  # Do any computation here math.factorial(100)
        time.sleep((0.9 - percent_cpu))


def f2(x, load, new_list, totalRAM, MemToFillMore, t):
    #print('memload=', MemToFillMore)
    percent_cpu = load / 100
    new_list.append([0] * int((10 ** 6 * 11) * totalRAM / 8) * int(MemToFillMore))
    timeout = time.time() + x
    while time.time() < timeout:
        start_time = time.process_time()
        while time.process_time() - start_time < percent_cpu:
            x = 1 * 1  # Do any computation here math.factorial(100)
        time.sleep((0.9 - percent_cpu))


def LoadCPU(percent, memload, timetoload):
    global newlist
    currentMemory = virtual_memory().percent
    totalRAM = round(virtual_memory().total / (2 ** 30))
    MemToFill_percent = memload
    MemToFillMore = int(MemToFill_percent - currentMemory)
    load = percent
    t = timetoload
    processes = cpu_count()
    print('utilizing %d cores\n' % processes)
    if memload < 0:
        pool = Pool(processes)
        func = partial(f, t, load)
        pool.map(func, range(processes))
    else:
        pool = Pool(processes)
        func = partial(f2, t, load, newlist, totalRAM, MemToFillMore/8)
        pool.map(func, range(processes))
        newlist.clear()
    return


if __name__ == '__main__':
    if sys.platform.startswith('win'):
        multiprocessing.freeze_support()
    choice = int(sys.argv[1])
    percent = int(sys.argv[2])
    timetoload = int(sys.argv[3])
    if choice == 1:
        LoadMemory(percent, timetoload)
    elif choice == 2:
        LoadCPU(percent, -1, timetoload)
    elif choice == 3:
        memload = int(sys.argv[4]) + 3
        LoadCPU(percent, memload, timetoload)
    elif choice == 4:
        sys.exit()
    else:
        print('Enter a valid choice')
