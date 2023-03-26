import os,psutil,sys
import time
def get_process_byname(name):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        process_name = p.name()
        if name in process_name:
            print(p.cmdline())
            print("Process name is: %s, pid is: %s" % (process_name, pid))
            return p


if __name__ == "__main__":
    while True:
        time.sleep(3)
        p = get_process_byname("sse")
        if p is None:
            continue
        memInfo = p.memory_info()
        print (memInfo.rss/1024,'k')


