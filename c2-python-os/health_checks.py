import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print("check_disk_usage: " + str(free))
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("check_cpu_usage: " + str(usage))
    return usage < 75

if not check_disk_usage("C:/") or not check_cpu_usage():
    print('ERROR!')
else:
    print(">Everything is OK!")