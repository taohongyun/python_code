
#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
def n():
    num = int(input("输入："))
    a = num // 10000
    b = num % 10000 // 1000
    c = num % 1000 // 100
    d = num % 100 // 10
    e = num % 10
    if a!=0:
        print("五位数",e,d,c,b,a)
    elif b!=0:
        print("四位数",e,d,c,b)    #因为 a!=0 在if条件中存在，所以在下边的elif b!=0 的条件中不需要加 a=0,下同。
    elif c!=0:
        print("三位数",e,d,c)
    elif d!=0:
        print("两位数",e,d)
    else:
        print("一位数",e)
n()
