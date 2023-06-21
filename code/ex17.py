from sys import argv

from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file,'rb') #加'rb' :编码格式不对，改为utf-8格式打开
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Read, hit RETURN to continue,CTRL-C to abort")
input()

out_file = open(to_file,'w') #以写入模式打开文件
out_file.write(indata) #将变量 indata 中的数据写入你想要的 to_file 中

print("Alright, all done.")

out_file.close()
in_file.close()