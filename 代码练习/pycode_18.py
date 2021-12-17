
for i in range(4):   #从0到3一共四行
    for j in range(2-i+1):
        print(" ",end="")   #依次不换行打印出*前空白内容
    for k in range(2*i+1):
        print("*",end="")   #依次不换行打印出对应数量的*
    print("")   #换到下一行
for x in range(3):  #从0到2一共三行
    for y in range(x+1):
        print(" ",end="")    #依次不换行打印出*前空白内容
    for z in range(4-2*x+1):
        print("*",end="")    #依次不换行打印出对应数量的*
    print("")  #换行

