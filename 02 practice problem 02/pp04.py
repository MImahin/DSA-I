# 4: Binary Search in a Sorted Array
# Problem: Implement binary search in a sorted array to locate a target value. Return the
# index of the target if found; otherwise, return -1.
# Example:
# Input: arr = [1, 3, 5, 7, 9], target = 5
# Output: 2

def search (arr , target ):
    low=0
    high = len(arr)-1
    
    while low<=high :
        mid=(high+low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
print(search( [1, 3, 5, 7, 9],5))
print(search( [1, 3, 5, 7, 9],9))
print(search( [1, 3, 5, 7, 9],1))
print(search( [1, 3, 5, 7, 9],0))
print(search( [1, 3, 5, 7, 9],16))
print(search( [1, 3, 5, 7, 9],3))