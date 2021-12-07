
#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……

n = int(input("输入"))

def num(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    nums = [0,1]
    for i in range(2,n):
        nums.append(nums[-1]+nums[-2])
    return nums
print(num(n))


