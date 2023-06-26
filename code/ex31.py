# This program prompts the user with a choice between two doors.
print("""You enter a dark room with two doors.
Do you go through door #1 #2 or door #3?""")

# The user's input is stored in the variable 'door'.
door = input("> ")

# If the user chose door #1...
if door == "1":
    # ...print a message...
    print("There's a giant bear here eating a cheese cake.")
    # ...ask the user a question...
    print("What do you do?")
    print("1. Take the cake.")
    print("2.Scream at the bear")
    # ...and store the user's input in the variable 'bear'.
    bear = input("> ")
    # If the user chose to take the cake...
    if bear == "1":
        # ...print a message and end the game.
        print("The bear eats your face off. Good job!")
    # If the user chose to scream at the bear...
    elif bear == "2":
        # ...print a message and end the game.
        print("The bear eats your legs off. Good job!")
    # If the user chose something else...

    elif bear == "3":
        print("the bear eat you brain")
    
    else:
        # ...print a message and continue the game.
        print(f"well, doing {bear} is probably better. Bear runs away.")
        print("Bear runs away.")
# If the user chose door #2...
elif door == "2":
    # ...print a message...
    print("You stare into the endless abyss at Cthulhu's retina.")
    # ...ask the user a question...
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    # ...and store the user's input in the variable 'insanity'.
    insanity  = input("> ")
    # If the user chose either blueberries or yellow jacket clothespins...
    if insanity == "1" or insanity =="2":
        # ...print a message and end the game.
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
# If the user chose something else...
elif door == "3":
    print("luckly,you hava a gun! you kill bears and eat their hands")
else:
    # ...print a message and end the game.
    print("You stumble around and fall on a knife and die. Good job!")
