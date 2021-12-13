
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
Count = int(input("请输入落地次数"))
Height = int(input("请输入起始高度"))
height = Height
path = height
for num in range(1,Count+1):
    if num == 1:

        path = path
    else:
        Height /= 2
        path = path + 2 * Height


print(f"{height}高度自由落下，他在第{Count}次时，共经过了{path}米，第{Count}次反弹高度为{Height}米")


