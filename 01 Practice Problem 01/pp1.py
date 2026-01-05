# Find the k
# th
# smallest element from an array.


def findKsmall (arr,k):
    if k>len(arr):
        return None 
    # Selection sorting technique
    for i in range(k):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr[k-1] 

    

print(findKsmall([5,4,3,2,1],4))