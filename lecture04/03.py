import random


def is_sorted(arr):
    l = len(arr)
    for i in range(0, l-1):
        if arr[i+1] < arr[i]:
            return False
    return True


def bogo(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


с = [2, 6, 9]
print(bogo(с))
