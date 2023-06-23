"""
Python warm up with recursion
"""

arr1 = []
arr2 = []
LENGTH = 8


def fibs(n):
    """Fibonacci Sequence with a loop"""
    for x in range(n - 1):
        if len(arr1) == 0:
            arr1.extend([0, 1])
        else:
            arr1.append(arr1[x - 1] + arr1[x])


# fibs(LENGTH)
# print(arr1)


def fibs_rec2_num(n):
    """Fibonacci Sequence with a recursive helper function first try"""
    if n == 0:
        return "Error"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibs_rec2_num(n - 2) + fibs_rec2_num(n - 1)


def fibs_rec2(n):
    """Fibonacci Sequence with a recursive function first try"""
    if n == 2:
        return [0, 1]
    ret = fibs_rec2(n - 1)
    ret.append(fibs_rec2_num(n))
    return ret


# print(fibs_rec2(LENGTH))


def fibs_rec(n):
    """Fibonacci Sequence with a recursive function optimized"""
    if n == 0:
        return "Error"
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    ret = fibs_rec(n - 1)
    ret.append(ret[-2] + ret[-1])
    return ret


# print(fibs_rec(LENGTH))


def merge(left, right):
    """Merge two arrays together"""
    return_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            return_arr.append(left.pop(0))
        else:
            return_arr.append(right.pop(0))

    if len(left) > 0:
        return_arr.extend(left)
    if len(right) > 0:
        return_arr.extend(right)

    return return_arr


def merge_sort(arr):
    """Returns a sorted array that is sorted with merge sort"""
    if len(arr) < 2:
        return arr

    mid = int(len(arr) / 2)
    left = arr[0:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([-9, 1, 3, 2, 4, 0]))
