# Find the Longest Consecutive Subsequence after sorting an array.


def findCsS(arr):
    # selection sort

    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    max=0
    track=1
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] == 1:
            track+=1
        elif arr[i+1]-arr[i]==0:
            continue
        else:
            if max<track:
                max=track
            track=1
    if max<track:
        max=track
    return max


print(findCsS([1, 9, 3, 10, 4, 20, 2]))
print(findCsS([3,2,2,2,1]))