

arr = [254, 44, 88, 35, 77, 645]


def bubblesort(arr):
    for i in range(len(arr) - 1):

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                j += 1
    return arr


print(bubblesort(arr))