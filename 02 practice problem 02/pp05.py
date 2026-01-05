# 5: Binary Search in Descending Order Array
# Problem: Perform binary search on a descending order sorted array to find a target value.
# Example:
# Input: arr = [9, 7, 5, 3, 1], target = 7
# Output: 1

def search (arr , target ):
    low=0
    high = len(arr)-1
    
    while low<=high :
        mid=(high+low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            high=mid-1
        else:
            low=mid+1
    return -1
print(search( [9, 7, 5, 3, 1],7))
