

def sum(L):
    if not L:    #当列表为空时，返回0
        return 0
    else:
        return L[0]+sum(L[1:])
print(sum([1,2,3,4,5,6,7,8,9]))
print(sum([]))

def sum(q):
    return 0 if not q else q[0]+sum(q[1:])  #如果列表为空的话返回0，否则返回列表第一位的值和列表其他所有值的和
print(sum([1,2,3,4,5,6,7,8,9]))

def sum(w):
    return w[0] if len(w) == 1 else w[0] + sum(w[1:])     #如果列表只有一位就返回第一位的值，否则就返回第一位的值和列表其它所有的和
print(sum([1,2,3,4,5,6,7,8,9]))