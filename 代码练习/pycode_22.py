 #利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def output(a,b):
#     if b == 0:
#         return
#     print(a[b-1])
#     output(a,b-1)
#
# a = [1,2,3,4,5]
# b = len(a)
# output(a,b)

#冒泡排序
arr = [254, 44, 88, 35, 77, 645]
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             (arr[j],arr[j+1]) = (arr[j+1],arr[j])
# print(arr)

#插入排序
for i in range(1,len(arr)):
    for j in range(1,len(arr)):
        if arr[j] < arr[j-1]:
            (arr[j],arr[j-1]) = (arr[j-1],arr[j])
print(arr)