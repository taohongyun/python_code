
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5



# def reduceNum(n):
#     print (f'{n} = ', end=" ")
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print (f'{n}')
#     while n not in [1] : # 循环保证递归
#         for index in range(2, n + 1) :
#             if n % index == 0:
#                 n //= index # n 等于 n//index
#                 if n == 1:
#                     print (index )
#                 else : # index 一定是素数
#                     print ('{} *'.format(index), end=" ")
#                 break
# reduceNum(2)
# reduceNum(100)


def num(n):
    print(f"{n}=",end ="")
    if not isinstance(n,int) or n<=0:
        print("请输入正确的数数字")
    elif n in [1]:
        print(f"{n}")
    while n not in [1]:
        for index in range(2,n+1):
            if n % index == 0:
                n //= index
                if n == 1:
                    print(index)
                else:
                    print(f"{index}*",end="")
                break

num(100)
num(101)