#creat a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville',   
}
cities['NY'] = "New York"
cities['OR'] = 'portland'
# add some more cities
print("_" * 10)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])

#print some states
print("_" * 10)
print("Mechigan's state has:",cities['MI'])
print("Florida's state has:",cities['FL'])

#do it using the state then cities dict
print("_"  * 10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbreviation
print("_" * 10)
for state, abbrev in list (states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print("_" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print("_" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("_" * 10)
#safely get a abbreviation by state that might not be there
satte = states.get("Texas")

if not satte:
    print("sorry, no Texas.")

#get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")