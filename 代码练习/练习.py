

def quicksort(arr,start,end):

    if start >= end:
        return
    pivot = arr[start]
    l = start
    r = end
    while l < r:
        while l<r and arr[r]>pivot:
            r-=1
        arr[l] = arr[r]
        while l<r and arr[l]<pivot:
            l+=1
        arr[r] = arr[l]
    arr[r] = pivot
    quicksort(arr,start,r-1)
    quicksort(arr,r+1,end)
    return arr

li = [84,54,26,48,2568,47,1]
a = quicksort(li,0,len(li)-1)
print(a)

