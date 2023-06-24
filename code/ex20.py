from sys import argv
# 从命令行参数中获取脚本名和输入文件名
script, input_file = argv

# 定义一个函数，用于打印整个文件内容
def print_all(f):
    print(f.read())

# 定义一个函数，用于将文件指针移动到文件开头
def rewind(f):
    f.seek(0)

# 定义一个函数，用于打印指定行数的文件内容
def print_a_line(line_count,f):
    print(line_count,f.readline()) # readline() 里面的代码能够扫描文件的每个字节，当它发现一个 \n 字符

# 打开输入文件并将文件对象赋值给变量 current_file
current_file = open(input_file)

print("First let's print the whole file: \n")

# 调用 print_all 函数打印整个文件内容
print_all(current_file)

print("Now let's rewind, kind like a tape.")

# 调用 rewind 函数将文件指针移动到文件开头
rewind(current_file)

print("Let's print three lines:")

# 设置当前行号为 1，调用函数 print_a_line() 打印当前行内容
current_line = 1
print_a_line(current_line, current_file)

# 将当前行号增加 1，调用函数 print_a_line() 打印当前行内容
current_line = current_line + 1
# current_line += 1
print_a_line(current_line, current_file)

# 将当前行号增加 1，调用函数 print_a_line() 打印当前行内容
current_line = current_line + 1
print_a_line(current_line, current_file)

#seek() 函数是用于在文件对象中移动文件指针的方法
