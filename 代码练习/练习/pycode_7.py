
#每隔一秒输出列表一个元素：

import time
a = [1,2,3,4]
for i in range(len(a)):
    print(i)
    time.sleep(i)