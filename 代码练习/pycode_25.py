
#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

num = int(input("请输入数字"))
a = num // 10000
b = num % 10000 // 1000
c = num % 1000 // 100
d = num % 100 // 10
e = num % 10
if a == 0 or a > 9:
    print("请输入五位数！")
elif a == e and b == d:
    print("这是回文数！")
else:
    print("这不是回文数！")