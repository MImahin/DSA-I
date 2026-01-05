# 3: Linear Search with Condition
# Problem: Find the first element in an array of integers that is greater than a given target. If
# no such element exists, return -1.
# Example:
# Input: arr = [3, 5, 7, 2, 8, 10], target = 6
# Output: 7

def search(arr,target):
    for i in arr:
        if i>target :
            return i
        
    return -1

print(search( [3, 5, 7, 2, 8, 10],6))
print(search( [3, 5, 7, 2, 8, 10],20))