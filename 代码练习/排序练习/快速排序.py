#   快速排序
def quicksort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    l = start
    r = end
    while l < r:     #当lr相交的时候停止循环
        while l < r and arr[r] >= pivot:
            r -= 1
        arr[l] = arr[r]     #当l<r，r位置的值比设置的基准值大的时候，r前进一位，直到小于等于基准值的时候，将r位置上的值赋予到l位置上
        while l < r and arr[l] <= pivot:
            l += 1
        arr[r] = arr[l]     #当l<r，l位置的值小于设置的基准值，l后退一位，直到大于等于基准值的时候，将l位置上值赋予到r位置上
    arr[r] = pivot
    quicksort(arr, start, r - 1)
    quicksort(arr, r + 1, end)
    return arr    #通过调用 quicksort() 函数，对lr相交位置的左右两边进行递归操作，返回列表arr


li = [-4,54,4875,14,-18,-10]
a = quicksort(li, 0, len(li) - 1)
print(a)
