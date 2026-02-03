import time

data=[i for i in range(30_000_000)]    


def binary_search(data, target, low, high):
    """A simple binary search"""
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            # print("Found")
            return True
        elif target < data[mid]:
            # print("Again...")
            return binary_search(data, target, low, mid-1)
        else:
            # print("Again...")
            return binary_search(data, target, mid+1,high)


a = time.time()

binary_search(
    data=data,
    target=12,
    low=0,
    high=len(data)
)

b = time.time()

print(f"Runtime using binary search {b-a} seconds")


def manual(data, target):
    for i in data:
        if i == target:
            return True
        


c = time.time()

manual(data = data, target=12)

d = time.time()

print(f"Runtime using manual {d-a} seconds")


print(f"BS / M ratio : {((b-a)/(d-c))} times")




