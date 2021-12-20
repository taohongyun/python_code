
#利用递归方法求5!。

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


print(fact(2)) # fact()为递归函数



