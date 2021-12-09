
#输入一串字符，判断里边有几个字母几个空格几个数字。

import string

strs = input("请输入你的字符串：")
a = 0
b = 0
c = 0
d = 0
e = 0
for str in strs:
    a+=1
    if str.isalpha():
        b+=1
    elif str.isspace():
        c+=1
    elif str.isdigit():
        d+=1
    else:
        e+=1
print(f"一共有{a}个字符，有{b}个字母，有{c}个空格，有{d}个数字，其它的还有{e}个")