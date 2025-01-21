from random import choice
# virtual bartender
drinks = ["vodka", "whiskey", "gin", "tequila", "rum", "rakija", "sake"]
print("Welcome to the virtual pub")
name = input("I am the virtual bartender, how do i call you? ")
try:
    age = input(f"How old are you,{name}?")
    age = int(age) # try to convert to a number
    if age >=  21:
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f"Where are you from,{name}?")
        legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and country != "USA":
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
    if age >120 or age < 5:
        print("Please do not lie to the virtual bartender")
    elif legal:
            print("You are allowed to drink")
            print(f"Here is a {choice(drinks)}")
    else:
            print(f"Dear {name}, I am  not allowed to serve you")
except ValueError:
    print("Please give a valid age")