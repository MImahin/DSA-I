# Problem: Given an array of integers, find the first occurrence of a target integer. If the target
# is not in the array, return -1.
# Example:
# Input: arr = [5, 3, 8, 1, 9], target = 8
# Output: 2


def search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1


print(search( [5, 3, 8, 1, 9],8))

print(search( [5, 3, 8, 1, 9],4))