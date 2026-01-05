# Linear Search with Multiple Occurrences
# Problem: Given an array, find all the indices where a target integer appears. Return an array
# of indices. If the target does not appear, return an empty array.
# Example:
# Input: arr = [4, 2, 3, 2, 4, 2], target = 2
# Output: [1, 3, 5]

def search(arr,target):
    a=[]
    for i in range(len(arr)):
        if arr[i]==target:
            a.append(i)
    return a

print(search( [4, 2, 3, 2, 4, 2],2))

print(search( [4, 2, 3, 2, 4, 2],9))