import os,psutil,sys
import time
def get_process_byname(name):
    pids = psutil.pids()
    pss = []
    for pid in pids:
        p = psutil.Process(pid)
        process_name = p.name()
        if name in process_name:
            print(p.cmdline())
            print("Process name is: %s, pid is: %s" % (process_name, pid))
            pss.append(p)
    return pss


if __name__ == "__main__":
    while True:
        memuse = 0
        time.sleep(1)
        ps = get_process_byname("klee")
        for p in ps:
            memInfo = p.memory_info()
            memuse += memInfo.rss/1024
        print (memuse,'k')

