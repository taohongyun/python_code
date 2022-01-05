

# 使用函数调用，输出三次 hello

def hello_1():
    print("hello")


def hello_2():
    for i in range(3):
        hello_1()
hello_2()


# 输入100以内的素数

for num in range(2,101):
    for nums in range(2,num):
        if num % nums == 0:
            break
    else:
        print(num)

