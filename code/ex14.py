from sys import argv #导入 'sys' 模板中的 'argv' 对象
#argv 是一个命令行参数列表，它包含了传递给python脚本的命令行参数
script, user_name,mac_name= argv

prompt = ">>>"

print(f"Hi {user_name},I\'m the {script} script")
print("I'd like to ask you few questions")
print(f"my name is {mac_name}")

print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"where do you live {user_name}")
lives = input(prompt)

print("waht kind of computer ddo you have?")
computer = input(prompt)

print("what is your favourite food")
food = input(prompt)

print(f"""
Alright, so you said {likes} about liking me .
You are live in {lives}. Not sure where that is.
And you have {computer} computer.
Your favour food is {food}\nnice.
""")