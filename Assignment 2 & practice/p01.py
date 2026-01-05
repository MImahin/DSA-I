
# bubble

# def sort(arr):
#     iter=0
#     for i in range(len(arr)):
#         flag=False
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#                 flag=True
#             iter+=1
#         if flag==False:
#             break
        
#     return arr,iter
            


# my try reverse bubble


# def sort(arr):

#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[j],arr[i]=arr[i],arr[j]
        
#     return arr


# select


# def sort(arr):

#     for i in range(len(arr)):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[min]>arr[j]:
#                 min=j
#             arr[i],arr[min]=arr[min],arr[i]
        
#     return arr


# insertaTION

# def sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]> key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key






#     return arr




def sort(arr):

    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if (arr[min][1]-arr[min][0])>(arr[j][1]-arr[j][0]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr


print(sort([(2, 5), (1, 2), (4, 6)]))
 

