import os,psutil,sys

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
    p = get_process_byname("sse")
    if p is None:
        sys.exit(0)
    cmds = p.cmdline()
    moduleName = ""
    for cmd in cmds:
        if ".bc" in cmd:
            moduleName = cmd
            break
    while True:
        os.system("sleep 1")
        p = get_process_byname("overflow")
        memInfo = p.memory_info()
        print (memInfo.rss/1024,'k')


