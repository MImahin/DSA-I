# linear search


# def search (arr,n):
#     for i in range (len(arr)):
#         if arr[i]==n:
#             return i
#     return -1





# binary search
# for sorted arr
def search (arr):
    low=0
    high=len(arr)-1
    while low<=high :
        mid=(low+high)//2
        if mid==0 or mid== len(arr)-1:
            return arr[mid],mid


        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return arr[mid],mid
        elif arr[mid]<arr[mid+1]:
            low=mid+1

        else:
            high=mid-1

    return None,-1

print(search([1, 3, 8, 12, 4, 2]))

print(search([1, 3, 8, 12]))

print(search([10,12, 4, 2]))

print(search([1, 3, 8, 12, 4, 2]))