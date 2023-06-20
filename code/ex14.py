from sys import argv
print("在命令行（终端）输入 'python ex14.py your_user_name' 来运行程序 ")
script, user_name = argv

prompt = "> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few question")
print(f"Do you loke me {user_name} ?")
likes = input(prompt)

print(f"where do you live {user_name}")
lives = input(prompt)

print("what kind of computer do you like?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. 
And you have a {computer} computer.
Nice.
""")
# 1、Zork I是电子游戏历史上最早的一款文字冒险游戏，是Colossal Cave Adventure的一个早期后继
# 2、修改第三行input() 括号内的内容 如：prompt = input(>>>)
# 3、 I'm sure