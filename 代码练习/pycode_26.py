
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# :Sunday(星期日)、Monday(星期一)、Tuesday(星期二)、Wednesday(星期三)、Thursday(星期四)、Friday(星期五)、Saturday(星期六)
def w():
    week = input("请输入：")
    if week[0] == 'S':
        if week[1] == 'u':
            print("这是星期日")
        else:
            print('这是星期六')
    elif week[0] == "M":
        print('这是星期一')
    elif week[0] == "T":
        if week[1] == 'u':
            print("这是星期二")
        else:
            print('这是星期四')
    elif week[0] == "W":
        print('这是星期三')
    elif week[0] == "F":
        print('这是星期五')
    else:
        print('请检查输入内容')
w()



