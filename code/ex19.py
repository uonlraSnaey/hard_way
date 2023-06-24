def chees_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} box of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
chees_and_crackers(20,30)

print("OR, we can variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

chees_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
chees_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
chees_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

def hello(pname):
    print(f"hello {pname}")
pname = input("name:")

hello(pname) 