import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline() # 这段代码表示从名为 language_file 的文件中读取一行文本并将其赋值给变量 line。

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, error)
    
# 打印出对应字符串经过编码和解码后的字节序列和字符串结果
def print_line(line, encoding, errors):
    next_lang = line.strip() # 用于去除字符串两端的空白字符（包括换行符、制表符、空格等）并返回处理后的新字符串。
    raw_bytes = next_lang.encode(encoding, errors = errors) # encode() 是字符串对象的方法，用于将字符串编码为指定的字节序列。
    cooked_string = raw_bytes.decode(encoding, errors = errors)# decode() 是字节对象的方法，用于将字节数据解码为指定的字符串。

    print(raw_bytes, "<==>", cooked_string)


languages = open("languages.txt", encoding = "UTF-8")

main(languages, encoding, error)

# 终端输入 python file_naem.py <encoding> <error>
# example :python ex23.py utf-8 namereplace  