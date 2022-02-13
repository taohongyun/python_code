
#题目形式：有一个楼梯，总共有10级台阶，每次只能走一级或者两级台阶，全部走完，有多少种走法？

def stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    i = 3
    while n >= i:
        a, b = b, a + b
        i += 1
    return b

print(stairs(10))


def stairs_1(n):
    if n <= 2:
        return n
    else :
        a = 1
        b = 2
        temp = 0
        for i in range(3,n+1):
            temp = a + b
            a = b
            b = temp

    return temp
print(stairs_1(10))