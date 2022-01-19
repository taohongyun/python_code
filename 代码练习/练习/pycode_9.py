#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score = int(input("请输入你的成绩"))
if score >= 90:
    grade = "优秀"
elif score >= 60:
    grade = "良好"
else :
    grade = "差"
print(f"你输入的{score},等级为{grade}")