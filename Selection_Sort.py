def selectin_sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i] #swqp
    return arr


arr=[3,6,9,2,1,0]
print(selectin_sort(arr))