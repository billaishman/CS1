#Bill Aishman
#Function Mash Up
#4/07/2024
#Bugs -
#challenges
# 1) Reorganize functions #5 and 6 to improve their efficiency
# 2) Takes a string and reverses it
# 3) Takes a string and checks whether it is a palindrome
# 4) Takes a name and returns the initials
#Sources - Python.org

# this imports the random library
import random

# 1. Two functions to reduce the number of print statements needed to “sing” a song
# this defines a function that will be the chorus
def chorus():
    print ("music")
    print ("is someone getting the best,the best, the best")
    print ("The best of you?")

# this defines a function that will print some lines and calls the function chorus()
def sing_song():
    print ("music")
    print ("lyrics")
    chorus()
    print ("lyrics")
    print ("music")
    chorus()
    print ("music")
    print ("lyrics")
    chorus()
    print ("oh")

# 2. Takes two numbers and prints their sum
# this defines a function that will add two variables
def addition(num1, num2):
    print("The sum:", num1 + num2)

# 3. Takes a list and prints every element in that list individually (vertically)
# this defines a function that will print every element of a list individually
def print_elements(listone):
    for element in listone:
        print(element)

# 4. Takes a list and an element and returns a boolean determined by whether the element is in the list
# this defines a function that will check if an element is in a list
def contains_element(listtwo, element):
    if element in listtwo:
        return True
    else:
        return False
    
# 5. Takes in a parameter and returns a boolean determined by whether that parameter is an integer
# this defines a function that will get user input and then determines if it is an integer
def get_integer(order):
    while True:
        number = input(f"Please enter the {order}: ")
        check_number = number
        
        if "-" in number:
            check_number = number[1:]
        if check_number.isnumeric():
            number = int(number)
            return number
        else:
            print("Please enter a number!")

# 6. Prompts the user for two numbers and prints a random number between the two. Use the previous function
# this defines a function that will find a random number between two others
def randomnum():
    lower_boundary = get_integer("lower boundary")
    upper_boundary = get_integer("upper boundary")
    print (random.randint(lower_boundary, upper_boundary))

# 7. Takes a string and two characters, then replaces every instance in the string of the first character with the second (without using string methods).
# this defines a function that will replace a letter in a phrase
def replaceletter():
    phrase = input("Please enter phrase: ")
    letter1 = input("Please enter letter to replace: ")
    letter2 = input("Please enter replacement letter: ")
    result = ""
    for i in phrase:
        if i == letter1:
            result += letter2
        else:
            result += i
    print ("The new phrase is: ", result)

# Challenges
# 1. Reorganize functions #5 and 6 to improve their efficiency
# 2. Takes a string and reverses it
# this defines a function that will take a string and reverse it
def reversestring(string1):
    revstring1 = ""
    for char in string1:
        revstring1 = char + revstring1
    print ("Your string reversed is: ", revstring1)

# 3. Takes a string and checks whether it is a palindrome
# this defines a function that will take user input and check if it is a palindrome
def palindrome():
    palindromestring = input("Please enter a string to see if it is a palindrome:")
    revstring2 = ""
    for char in palindromestring:
        revstring2 = char + revstring2        
    if palindromestring == revstring2:
        print ("It is a palindrome!")
    else:
        print ("Not a palindrome!")
    
# 4. Takes a name and returns the initials
# this defines a function that will take user input and take the first letters of a string and print them
def nameinitials():
    nameinitials1 = input("Please enter a two word name to get initials:")
    first, last = nameinitials1.split(' ')
    print (first[0],".",last[0],".")
    
def main():
    print ("1) Make a song")
# this calls the sing_song() function
    sing_song()
    print()
# this calls the addition() function
    print ("2) Make an addition equation")
    num1 = get_integer("first number")
    num2 = get_integer("second number")
    addition(num1, num2)
    print()
# this section makes a list and then prints it vertically
    print ("3) Make a list and print it")
    listone = ["chicken","steak","pork","food"]
    print_elements(listone)
    print()
# this sections defines a list and then checks if and element is in a list
    print ("4) Make a list and return a boolean")
    listtwo = ["water","milk","4","9","smoothie","1"]
    contains_element(listtwo, "milk")
    contains_element(listtwo, "bill")
    print("5) Returns a boolean determined by whether that parameter is an integer.")
    print ("6) Take 2 numbers and print a random number between them.")
# this calls the randomnum() function to generate a random number between two other user entered numbers
    randomnum()
    print()
    print ("7) Take a string and replace a letter.")
# this calls the replaceletter() function to replace a letter in a string entered by the user
    replaceletter()
    print ()
    print ("Challenges!")
# this calls the reversestring() function to reverse a string the user enters
    string1 = input("Please enter a string to reverse:")
    reversestring(string1)
    print ()
# this calls the palindrome() function to see if a phrase is a palindrome
    palindrome()
    print ()
# this calls the nameinitials() function to take the first letters of a two word string and print their first letters    
    nameinitials()
    print ()
main()
