# 10: Find Peak Element with Binary Search
# Problem: Given an array where elements increase and then decrease (a ”mountain” array),
# find the index of the peak element using binary search.
# Example:
# Input: arr = [1, 3, 8, 12, 4, 2]
# Output: 3 (peak element 12 is at index 3)

def search (arr ):
    low=0
    high = len(arr)-1
    
    while low<=high :
        mid=(high+low)//2
        if mid==0:
            if arr[mid+1]>arr[mid]:
                return mid+1
            else:
                return mid
        elif mid==len(arr)-1:
            if arr[mid-1]>arr[mid]:
                return mid-1
            else:
                return mid
        else:
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid-1]>arr[mid] :
                high=mid-1
            else :
                low=mid+1


        

print(search( [1, 3, 8, 12, 4, 2]))

print(search( [1, 3, 8]))
print(search( [1, 3, 8, 12, 4, 2]))
print(search( [1, 3]))
print(search( [1, 3, 8, 12]))
print(search( [ 12, 4, 2]))