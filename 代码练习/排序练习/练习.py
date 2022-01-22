
#希尔排序
def shellsort(list):
    n = len(list)
    gap = n // 2

    while gap > 0:    #当gap等于1的时候停止//
        for j in range(gap,n):   #
            i = j
            while i > 0:
                if list[i] < list[i-gap]:
                    list[i],list[i-gap] = list[i-gap],list[i]
                    i -= gap
                else:
                    break    #
        gap //= 2

alist = [15,41,51,741,5,474,91,4]
a = shellsort(alist)
print(alist)

