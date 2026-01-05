# You are given a list of tasks, where each task is represented as
# (StartTime, FinishTime). The goal is to sort the tasks based on their
# durations (calculated as FinishTime - StartTime) in ascending
# order.

def sorting(arr):
    for i in range (len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if (arr[j][1])-(arr[j][0]) < (arr[min][1])-(arr[min][0]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    return arr

print(sorting([(2, 5), (1, 2), (4, 6)]))