arr = [254,44,88,35,77,645]
def insertionsort(arr):
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            if arr[j] < arr[j-1]:
                (arr[j-1],arr[j]) = (arr[j],arr[j-1])

    return arr

print(insertionsort(arr))



