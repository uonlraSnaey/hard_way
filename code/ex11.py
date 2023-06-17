print("How old are you?",end=" ")
age = input()
print("How tall are you?",end=" ")
height = input()
print("How much do you weight?",end=' ')
weight = input()

print("temp?")
tmp = float(input())


print(f"so you are {age} old, {height} tall and {weight} heavy.")
print("温度是：",tmp)
'''
input():
input()是一个内置函数，用于从用户那里获取输入。它允许程序在运行时与用户进行交互，接收来自用户的输入，并将其作为字符串返回给程序。
如果要返回其他类型的值,则需要进行类型转换

age = int(input("请输入您的年龄："))
next_year_age = age + 1
print("明年您将年满：" + str(next_year_age) + "岁")

weight = float(input("请输入您的体重（kg）："))
half_weight = weight / 2
print("您的一半体重是：" + str(half_weight) + "kg")


'''