def add(a, b):
    print(f"ADDINT {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MUTIPLYING {a} * {b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

# value_one = int(input("first value:"))
# # value_two = float(input("second value:"))
#age = add(a, b) 
#...........


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, IQ: {iq}")
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("The brcomes: ",what, "Can you do it by hand?")
