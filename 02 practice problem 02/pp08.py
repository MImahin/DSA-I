# Count Occurrences of Target with Binary Search
# Problem: In a sorted array, count the occurrences of a target value using binary search.
# Example:
# Input: arr = [2, 4, 4, 4, 6, 7], target = 4
# Output: 3


def search(arr, target):
    occur=[-1,-1]
    low= 0
    high =len(arr)-1
    while low<=high:
        mid=(low+high )//2
        if arr[mid]==target:
            occur[0]=mid
            high=mid-1
                
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
   
    low= 0
    high =len(arr)-1
    while low<=high:
        mid=(low+high )//2
        if arr[mid]==target:
            
            occur[1]=mid
            low=mid+1

        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    if occur==[-1,-1]:
        return 0
    return occur[1] - occur[0]+1


print(search( [2, 4, 4, 4, 6, 7],4))
print(search( [2, 4, 4, 4, 6, 7],6))
print(search( [2, 4, 4, 4, 6, 7],8))