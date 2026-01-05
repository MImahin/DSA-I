# Sort an array based on the frequency of its elements. If two
# elements have the same frequency, sort them in ascending order.



def sortfreq(arr):
    countdict={}
    for i in range((len(arr))):
        if arr[i] not in countdict:
            countdict[arr[i]]=1
        else:
            countdict[arr[i]]+=1

    newarr=[]
    for i in countdict.values():
        if i not in newarr:
            newarr.append(i)
    
    for i in range(1,len(newarr)):
        pick=newarr[i]
        j=i-1
        while j>=0 and newarr[j]<pick:
            newarr[j+1]=newarr[j]
            j-=1
        newarr[j+1]=pick
    newarr2=[]
    for i in newarr:
        nums=[]
        for k,v in countdict.items():
            if v==i:
                nums.append(k)
        if len(nums)>1:
            for i in range(1,len(nums)):
                pick=nums[i]
                j=i-1
                while j>=0 and nums[j]>pick:
                    nums[j+1]=nums[j]
                    j-=1
                nums[j+1]=pick

        for i in nums :
            for j in range(countdict[i]):
                newarr2.append(i)

    return newarr2        
            
            
print(sortfreq([4, 3, 1, 6, 1, 3, 4, 4]))  
print(sortfreq([9, 8, 7, 6]))  
print(sortfreq([3, 1, 2, 3, 1, 2]))  
print(sortfreq([10]))  
# technique/ algorithm

# make a dict whith all element as key and count as value
# make list of counts in decending order  skipped duplicate
# then loopng with each count appending elements to a new list by aceesing elements from the dict
# in case of more element with same count taking the list of those sorting in acending and the appending in that sequence    