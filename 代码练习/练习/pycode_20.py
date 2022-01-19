

#求1+2!+3!+...+20!的和。
# !是阶乘运算符
a = 1
b = 0
for i in range(1,21):
    a = a*i
    b += a
print(b)

