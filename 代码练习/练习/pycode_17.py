
#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

team2 = ["x","y","z"]
#
for i in range(len(team2)):
    for j in range(len(team2)):
        if i!=j:
            for k in range(len(team2)):
                if i!=k and j!=k:
                    if i!= 0 and k!= len(team2)-1 and k!=0:
                        print(f"a和{team2[i]},b和{team2[j]},c和{team2[k]}")

#
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))