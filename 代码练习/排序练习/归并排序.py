
def mergesort(list):
    n = len(list)
    if n <= 1:                       #如果列表list的数据数量小于等于1，或者列表拆分到数据数量小于等于1时，则直接返回列表内容
        return list
    m = n//2                         #取列表中间位置为m
    left = mergesort(list[:m])       #将原列表list中的0到m-1位置的内容设为新列表left
    right = mergesort(list[m:])      #将原列表list中的m到最后的内容设为新列表right
    l = 0                            #将left列表的起始索引命名为l
    r = 0                            #将right列表的起始索引命名为r
    result = []                      #设置一个新的空列表为result
    while l < len(left) and r < len(right):   #当left和right列表的索引值等于数据数量（也就是索引值大于数据数量-1）时,停止while循环
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1       #将left和right列表的第一位进行比较，较小的直接添加到result列表，然后索引值加1
    result += left[l:]
    result += right[r:]   #while循环结束后会剩一个无比较对象的最大值，将最大值添加到result列表中
    return result       #返回新列表result

li = [24,8565,4,8,5894,245,6,412]
a = mergesort(li)
print(a)    # 原列表拆分成新列表，所以要给赋予新变量进行打印
