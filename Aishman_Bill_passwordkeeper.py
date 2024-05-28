#Bill Aishman
#password keeper
#4/26/2024
#Bugs -
#challenges
# 1) Allow the user to retroactively add more usernames and passwords
# 2) Allow the user to change usernames and passwords
# 3) Generate a secure password for the user
# 4) Check password strength
# 5) Write to Excel file
#Sources - Python.org

# These libraries are for the secure password
import random
import string

# This library is to write to the Excel File
import csv

# This makes three parallel arrays: (1) websites and their (2) usernames and (3) passwords
password = []
username = []
websites = []

# This function check how complex/secure the passwords are
# if the password is less than 6 characters or all lower case 
def check_password(password):
    if len(password) <6:
        print ("Your password is short. It should be over 6 characters.")
    elif len(password) >=6:
        print ("Your password length is ok")
        if password.isupper() or password.islower() or password.isdigit():
            print ("Your password is weak. Try using uppercase, lowercase and a number.")
        else:
            print ("Your password is strong.")

# This function generates a secure password
def secure_password():
    password_answer = input("Do you want 1) make your own password 2) generate a secure password?")
    if password_answer == '1':
        passwordadd = input("make a password: ")
        password.append(passwordadd)
        check_password(passwordadd)
    else:
        source = string.ascii_letters + string.digits
        passwordadd = ''.join((random.choice(source) for i in range(6)))
        print("Your password is:", passwordadd)
        password.append(passwordadd)

# This function saves to the excel file
def save_to_file():
    file = open('mydata.xlsx', 'w')
    file = csv.writer(file)
    file.writerow(['website', 'username', 'password']) 
    for i in range (len(websites)):
        file.writerow([websites[i], username[i], password[i]])
    print('All records inserted successfully !')

# This function prompts the user to enter websites and their usernames and passwords to store in the parallel arrays above
def makewebsite():
    websitesadd = input("make a website: ")   
    usernameadd = input("make a username: ")
    secure_password()
    websites.append(websitesadd)
    username.append(usernameadd)

# This function:
# Allows the user to print out the list of websites along with their usernames and passwords.
# Allows the user to access a specific website’s username and password.
# Allows the user to end the program.

def question():
    while True:
        answer = input("what do you want to do?\n  1: print all enteries   2: print a specific website    3: add a website \n  4: end code   5: change username or password  6: Save to file \n type 1,2,3,4,5 or 6: \n")
        if answer == '1':
            for i in range (len(websites)):
                print(f" website: {websites[i]}, username: {username[i]}, password: {password[i]} \n")
        elif answer == '2':
            web = input("what website do you want to see?\n")
            if web in websites:
                i = websites.index(web)
                print(f" website: {websites[i]}, username: {username[i]}, password: {password[i]}\n")
        elif answer == '3':
            makewebsite()
        elif answer == '4':
            print ("thank you!")
            break
        elif answer == '5':
            PassOrUser = input("do you want to change a password or a username?: \n")
            if PassOrUser == 'password':
                Passchange = input("what password do you want to change?: \n")
                if Passchange in password:
                    Pi = password.index(Passchange)
                    password[Pi] = input("what do you want to change it to?: \n")
            elif PassOrUser == 'username':
                Userchange = input("what username do you want to change?: \n")
                if Userchange in username:
                    Ui = username.index(Userchange)
                    username[Ui] = input("what do you want to change it to?: \n")
        elif answer == '6':
            save_to_file()
            
def main():
    makewebsite()
    question()


main()
