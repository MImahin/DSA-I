# 3. Find the smallest difference of elements from an array.

def finDiff(arr):
    # Insertation sorting technique

    for i in range (1,len(arr)):
        picked=arr[i]
        j=i-1
        while (j>=0) and arr[j]>picked:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=picked

    min=arr[1]-arr[0]
    for i in range(0,len(arr)-1):
        if arr[i+1]-arr[i] < min :
            min =arr[i+1]-arr[i]
    return min

print(finDiff([1231,215,45,44231,1242,5534,213,89,44232]))
