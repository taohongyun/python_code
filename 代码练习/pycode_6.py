
#输出 9*9 乘法口诀表 end后的空格识别第一个for循环打印出来的空格

for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}", end=" ")


