i  = 0
number = []

while i < 6:
    print(f"At the top i is {i}")
    number.append(i)

    i = i + 1
    print("Number now:",number)
    print(f"At the bottom i is {i}")

print("The number:")

for num in number:
    print(num)

""" 
def while_loop(n)
i = 0
number = []

while i < n:
    print(f"At the top i is {i}")
    number.append(i)

    i = i + 1
    print("Number now:",number)
    print(f"At the bottom i is {i}")

print("The number:")

for num in number:
    print(num) 
    
while_loop(6)
print("----------")
while_loop(5)
    """

'''
def for_loop(n):
    number = []

    for i in range(n):
        print(f"At the top i is {i}")
        number.append(i)

        print("Number now:", number)
        print(f"At the bottom i is {i + 1}")

    print("The numbers:")

    for num in number:
        print(num)

# 调用函数并传入不同的数值进行测试
for_loop(3)
print("------------------")
for_loop(5)

#没有保留增加值(i = i + 1)
'''
