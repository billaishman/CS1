#Bill Aishman
#password keeper
#4/26/2024
#Bugs -
#challenges
#Sources - Python.org

import pandas as pd

password = []
username = []
websites = []
def makewebsite():
    websitesadd = input("make a website: ")   
    usernameadd = input("make a username: ")
    passwordadd = input("make a password: ")
    websites.append(websitesadd)
    username.append(usernameadd)
    password.append(passwordadd)

def question():
    while True:
        answer = input("what do you want to do?\n  1: print all enteries   2: print a specific website    3: add a website \n  4: end code   5: change username or password  \n type 1 or 2 or 3: \n")
        if answer == '1':
            for i in range (len(websites)):
                print(f" website: {websites[i]}, username: {username[i]}, password: {password[i]}\n")
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
def main():
    makewebsite()
    question()


main()
