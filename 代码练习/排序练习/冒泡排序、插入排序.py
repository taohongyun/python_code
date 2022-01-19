
#  冒泡排序
arr = [254, 44, 88, 35, 77, 645]


def bubblesort(arr):
    for i in range(len(arr) - 1):

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

    return arr


print(bubblesort(arr))


#   插入排序
arr = [254, 44, 88, 35, 77, 645]


def insertionsort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                (arr[j - 1], arr[j]) = (arr[j], arr[j - 1])

    return arr


print(insertionsort(arr))




