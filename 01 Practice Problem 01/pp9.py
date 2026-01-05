# 9. You are given two arrays a and b. Merge a and b into a single array
# sorted in non-decreasing order.


def mergesort(arr1,arr2):
    arr=arr1+arr2
    for i in range(len(arr)):
        flag=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                flag=True
        if flag==False:
            break
        

    return arr


print(mergesort([1,16,13,14,4],[15,12,5,3,7]))