# Sort an array by absolute value in ascending order.

def sortAbs(arr):
    # selection sorting technique

    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if abs(arr[j])<abs(arr[min]):
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    
    return arr
    
print(sortAbs([43,-423,13,-76,2]))