def speed():
    print("There is a speed test station")
    tested_people = 0

    while tested_people < 10:
        print("Your speed is:")
        speed_input = input("> ")

        try:
            speed_value = int(speed_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer value.")
            continue

        if speed_value > 30:
            print("You are too fast!")
            print(f"Your speed is {speed_value}")
        else:
            print("You are a good driver.")

        tested_people += 1
        print(f"You are the {tested_people} tested person.\n")

speed()
