from sys import argv

script, filename = argv

# 打开文件，如果文件不存在则自动创建
txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

## Add
txt.close()
txt_again.close()