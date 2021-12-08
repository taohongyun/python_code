
# 输入101到200任意数，判断是否为素数

# def num(i):
#     # for i in range(101,201):
#     a = int(0)
#     for j in range(2,i):
#         if i % j == 0:
#             a += 1
#     print(a)
#     if a > 0:
#         print(f"{i}不为素数")
#     else:
#         print(f"{i}为素数")
#
# num(101)


# 判断101-200之间有多少个素数，并输出所有素数。



for i in range(101,201):
    a = int(0)
    for j in range(2,i):
        if i % j == 0:
            a+=1

    if a == 0:
        print(f"{i},",end="")











