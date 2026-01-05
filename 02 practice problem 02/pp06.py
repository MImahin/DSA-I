# 6: Binary Search for First and Last Occurrence
# Problem: Given a sorted array, find the first and last positions of a target value. If the target
# is not found, return (-1, -1).
# Example:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: (1, 3)

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
    
    return occur[0],occur[1]
    
print(search([1, 2, 2, 2, 3, 4],2))

print(search([1, 2, 2, 2, 3, 4,5,5,5,5,5,5,5],5))
print(search([1, 2, 2, 2, 3, 4,5,5,5,5,5,5,5],9))