import os

def disk_usage(path: str):
    """ Calculate disk usage of any directory.
    Args : path
    Return : cumulative diskspace by all nested folder structure.
    """

    total = os.path.getsize(path)
    print("total disk usage initially : ",total)

    if os.path.isdir(path):
        for file in os.listdir(path=path):
            childPath = os.path.join(path,file)
            total += disk_usage(childPath)
            print(f"Disk usage for : {path} : {disk_usage(childPath)}")

    return total

d1 = disk_usage(path="/home/pritesh-jha/projects/dsa/2_oops")
print("----------------------------------------")
print("total disk usage : ",d1)

