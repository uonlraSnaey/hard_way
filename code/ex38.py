ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ') #将字符串 ten_things 拆分为一个列表，并将结果赋值给变量 stuff。
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #从列表 more_stuff 中移除并返回最后一个元素，并将其赋值给变量 next_one。
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print("-------------")
print(stuff[-1])
print("-------------")
print(stuff.pop())
print("-------------")
print(' '.join(stuff))
print("-------------")
print('#'.join(stuff[3:5]))