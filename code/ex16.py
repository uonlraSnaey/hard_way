"""
close - 关闭文件，就像编辑器中的 “文件->另存为”一样。
read - 读取文件内容。你可以把读取结果赋给一个变量。
readline - 只读取文本文件的一行内容。
truncate - 清空文件。清空的时候要当心。
write('stuff') - 给文件写入一些“东西”。
seek(0) - 把读/写的位置移到文件最开头。

"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that hit CREL-C(^c)")
print("If you do want that,hit ENTER")

input("?")

print("Opening thr file...")
target = open(filename,"w+") # 创建了一个名为 'target' 的文件对象，使用open() 的写入方式来打开文件
# 'w' 作为 open() 函数的第二个参数，表示以写入模式打开文件。若不曾存在，则创建新文件。

print("Truncating the file.Goodbye!")
target.truncate() #对文件对象 'target' 进行截断操作

print("Now I'm going to ask you fir three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
# add

print("Add finally, we close it.")
target.close()
# $python ex14.py file_name.txt

#add
txt = open(filename)
print(txt.read())
txt.close()