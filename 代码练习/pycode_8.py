
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for num in range(100,1000):
    j = num // 100
    q = num // 10 % 10
    k = num % 10
    if num == j*j*j + q*q*q + k*k*k:

        print(num)

#拓展 水仙花是一个四位数
# for num in range(1000,10000):
#     j = num // 1000
#     q = num // 100 % 10
#     k = num // 10 % 10
#     w = num % 10
#     if num == j*j*j+q*q*q+k*k*k+w*w*w:
#         print(num)