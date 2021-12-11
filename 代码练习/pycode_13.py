
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int(input("请输入您要输入的值："))
nums = int(input("请输入您输入的值的相加次数:"))
b = 0
c = 0
d = a
if nums % 2 == 0:
    for num in range(nums):

        if num+1 ==1:
            a = (d*(10**b))
            print(f"{a}+",end="")

        elif num+1 <= nums/2 and num!=0:
            a = (d*(10**b))+a

            print(f"{a}+", end="")
        elif num+1 == nums/2+1:
            a = a
            b = b
            print(f"{a}",end="")
        else:
            a=a//10
            print(f"+{a}", end="")
        b+=1
        c+=a


if nums % 2 != 0:
    for num in range(nums):

        if num+1 ==1:
            a = (d*(10**b))
            print(f"{a}+",end="")

        elif num+1 <= nums//2+1 and num!=0:
            a = (d*(10**b))+a
            print(f"{a}+", end="")
        elif num+1 <= nums//2+2 and num!=0:
            a=a//10
            print(f"{a}", end="")
        else:
            a=a//10
            print(f"+{a}", end="")
        b+=1
        c+=a
print(f"={c}")



