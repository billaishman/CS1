#Bill Aishman
#Morning Routine Program - A flowchart of morning decisions.
#11/10/2023
# Bugs - None
# Challenges - User errors addressed via while loops and input string conversions to lowercase
# Sources - https://www.python.org/, https://www.w3schools.com/python/

#This uses print command to print out some text
print("Good morning, Bill!")
print("This will help you decide what to do in the morning.")
print("\n")

#This runs a loop while the variable (raining) is not a yes or no
while True:
    print("Is it raining?")
    #This sets the variable (raining) to whatever the user inputs
    raining = input("Please enter yes or no: ")
    #if the user inputs "yes" then it types the text
    if raining.lower() == "yes":
        #this makes the input lowercase
        print("Do not bring lacrosse gear.")
        print("\n")
        break
    #if the user inputs "no" then it types the other text
    elif raining.lower() == "no":
        print("Pack lacrosse gear")
        print("\n")
        break
#if the user does not enter a "yes" or "no" it stays in the while loop

#these do the same loop with different variables
while True:
    print("Do you have math?")
    math = input("Please enter yes or no: ")
    if math.lower() == "yes":
        print("Bring your math binder.")
        print("\n")
        break
    elif math.lower() == "no":
        print("Do not bring math binder.")
        print("\n")
        break

while True:
    print("Are you hungry?")
    hunger = input("Please enter yes or no: ")
    if hunger.lower() == "yes":
        print("Eat breakfast!")
        print("\n")
        break
    elif hunger.lower() == "no":
        print("Bring breakfast, eat later!")
        print("\n")
        break

while True:
    print("Are you cold?")
    cold = input("Please enter yes or no: ")
    if cold.lower() == "yes":
        print("Bring your 1/4 zip!")
        print("\n")
        break
    elif cold.lower() == "no":
        print("Do not bring your 1/4 zip")
        print("\n")
        break

print("Done! Go to School!")


