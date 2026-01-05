# 5. Sort an Array of Strings according to length.


def sortlen(arr):
    # bubble sorting technique

    for i in range (len(arr)):
        flag=False
        for j in range(0,len(arr)-i-1):
            if len(arr[j+1])<len(arr[j]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
                flag= True
        if flag==False:
            break

    return arr


a = ["apple", "bat", "carrot", "dog"]

print(sortlen(a))