# 7: Find the Insert Position
# Problem: Given a sorted array, return the index where a target value should be inserted to
# maintain the order. Use binary search.
# Example:
# Input: arr = [1, 3, 5, 6], target = 4
# Output: 2

def search(arr,target):
    low=0
    high =len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]==target:
            return mid
        else:
            high=mid-1
    return low



print(search([10, 20, 30],5))