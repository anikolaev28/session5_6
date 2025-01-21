name = input("What is your name?? ")
print("hello", name)
age = input("How old are you? ",)
try:
    # another way to format print is via f-strings
    print(f"{name}, you were born in {2024-int(age)}")
    division = int(age) / 0
except ValueError:
    print("Age must be a valid number")
    print(f"The value that you typed was {age}")
except ZeroDivisionError:
    print("You can't divide by 0")
except:
    print("No idea what else can go wrong, but just in case.")
print(f"{name}, thanks for playing")

