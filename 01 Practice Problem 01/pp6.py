# Sort odd indexed elements of an array in descending order and
# even indexed elements in ascending order.

def sort(arr):
    od=[arr[i] for i in range(len(arr)) if i%2!=0]
    ev=[arr[i] for i in range(len(arr)) if i%2==0]

    for i in range(1,len(od)):
        pick=od[i]
        j=i-1
        while j>=0 and od[j]<pick:
            od[j+1]=od[j]
            j-=1
        od[j+1]=pick

    for i in range(1,len(ev)):
        pick=ev[i]
        j=i-1
        while j>=0 and ev[j]>pick:
            ev[j+1]=ev[j]
            j-=1
        ev[j+1]=pick
    newarr=[]
    for i in range(len(arr)):
        if i%2==0 :
            newarr.append(ev[i//2])
        else:
            newarr.append(od[i//2])
    return newarr

print(sort([16,17,4,18,1,20,5,12]))
print(sort([1,20,4,18,5,17,16,12]))






















#  wrong understanding but good one
def mixsort(arr):
    # insertation sorting
    for i in range(1,len(arr)):
        pick=arr[i]
        j=i-1
        while j>=0 and arr[j]>pick:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=pick

    sube=arr[:(len(arr)+1)//2]
    subo=arr[(len(arr)+1) //2:]
    newarr=[]
    for i in range(len(arr)):
        if i%2==0:
            newarr.append(sube[i//2])
        else:
            newarr.append(subo[-(i//2)-1])
            
    return newarr


# print(mixsort([7,5,4,3,6,2,1]))
# print(mixsort([16,17,4,18,1,20,5,12]))
# print(mixsort([4,3,2,1])) 