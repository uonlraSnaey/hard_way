type_of_people = 10
x = f"There {type_of_people}"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and tose who {do_not}"

print(x)
print(y)

print(f"I said :{x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "this is the left side of "
e = "a string with a right side"

print(w + e)