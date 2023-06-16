#定义字符串格式
formatter = "{} {} {}"

# 使用整数作为参数格式化字符串
print(formatter.format(1,2,3,4))

print(formatter.format("one","two","three","four"))

print(formatter.format(True,False,False,True))

# 使用字符串变量作为参数格式化字符串
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
'''
这段代码使用了字符串的format()方法来格式化字符串。
在这个例子中，我们定义了一个名为formatter的格式字符串，其中包含四个占位符{}。
然后，我们通过调用format()方法并传入相应的参数来替换这些占位符。
'''