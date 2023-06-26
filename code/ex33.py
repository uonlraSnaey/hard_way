# Initialize a variable to 0
i = 0

# Initialize an empty list
numbers = []

# Execute a loop as long as the value of i is less than 6
while i < 10:
    # Print a message with the current value of i
    print(f"At the top i is {i}")

    # Add the current value of i to the list
    numbers.append(i)

    # Increment the value of i by 1
    i = i + 2

    # Print the current state of the numbers list
    print("Numbers new: ", numbers)

    # Print a message with the current value of i
    print(f"At the bottom i is {i}")

# Print a message
print("The numbers:")

# Iterate through the numbers list and print each element
for num in numbers:
    print(num)
print("自定义函数调用numebrs list")
def create_number_list():
    numbers = []
    for i in range(0, 10):
        numbers.append(i)
    return numbers

my_number = create_number_list()
print(my_number)