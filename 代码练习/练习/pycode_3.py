
#输入年月日，确认是一年中的那天

year = int(input("year"))
mouth = int(input("mouth"))
day = int(input("day"))


mouths = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < mouth <=12:

    num = mouths[mouth-1]

num += day
days = 0
if year%400 ==0:
    days = 1
if (days==1) and (mouth>2):

    num += days
print(f"这是一年里的第{num}天")