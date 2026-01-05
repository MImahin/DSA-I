# Find Closest Element with Binary Search
# Problem: Given a sorted array, find the element closest to a given target. If two elements are
# equally close, return the smaller one.
# Example:
# Input: arr = [1, 3, 8, 10, 15], target = 12
# Output: 10


def search (arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return arr[mid] 

        elif arr[mid]<target:
            low=mid+1


        else:
            high=mid-1
    if mid==0:
        return arr[low]
    elif mid==len(arr)-1:
        return arr[low-1]
    else:
        if (target-arr[low-1])<=(arr[low]-target):
            return arr[low-1]
        else:
            return arr[low]




print(search([1, 3, 8, 10, 15],12))
print(search([1, 3, 8, 10, 15],16))
print(search([1, 3, 8, 10, 15],5))
print(search([1, 3, 8, 10, 15],2))