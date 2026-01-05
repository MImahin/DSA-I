# Find the median from an array.

# The median is the middle value when the numbers are arranged in order.

# If there's an odd number of values → the middle one.

# If there's an even number of values → the average of the two middle ones.

def median(arr):
    # bubble sorting technique
    n=len(arr)
    iter=0
    for i in range(n):
        flag=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
            iter+=1
        if  flag==False:
            break
    
    if n%2==0:
        med=(arr[n//2]+arr[n//2-1])/2
    else:
        med=arr[n//2]
    return med


print(median([9,17,15,11]))