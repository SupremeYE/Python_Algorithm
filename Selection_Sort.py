def selectin_sort(arr):
    for i in range(len(arr)-1):
        min_idx=i #가장 작은값을 고정값으로 설정
        for j in range(i+1, len(arr)): #작은값을 제외한 나머지 숫자와 비교
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i] #swap
    return arr


arr=[3,6,9,2,1,0]
print(selectin_sort(arr))