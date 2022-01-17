#
# #  冒泡排序
# arr = [254, 44, 88, 35, 77, 645]
#
#
# def bubblesort(arr):
#     for i in range(len(arr) - 1):
#
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j + 1]:
#                 (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
#
#     return arr
#
#
# print(bubblesort(arr))
#
#
# #   插入排序
# arr = [254, 44, 88, 35, 77, 645]
#
#
# def insertionsort(arr):
#     for i in range(1, len(arr)):
#         for j in range(1, len(arr)):
#             if arr[j] < arr[j - 1]:
#                 (arr[j - 1], arr[j]) = (arr[j], arr[j - 1])
#
#     return arr
#
#
# print(insertionsort(arr))


#   快速排序
def quicksort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    l = start
    r = end
    while l < r:     #当lr相交的时候停止循环
        while l < r and arr[r] > pivot:
            r -= 1
        arr[l] = arr[r]     #当l<r，r位置的值比设置的基准值大的时候，r前进一位，直到小于等于基准值的时候，将r位置上的值赋予到l位置上
        while l < r and arr[l] < pivot:
            l += 1
        arr[r] = arr[l]     #当l<r，l位置的值小于设置的基准值，l后退一位，直到大于等于基准值的时候，将l位置上值赋予到r位置上
    arr[r] = pivot
    quicksort(arr, start, r - 1)
    quicksort(arr, r + 1, end)
    return arr    #通过调用 quicksort() 函数，对lr相交位置的左右两边进行递归操作，返回列表arr


li = [84, 54, 26, 48, 2568, 47, 1]
a = quicksort(li, 0, len(li) - 1)
print(a)
