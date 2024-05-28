# Bill Aishman
# Rock Paper Scissors
# 12/1/2023
# Bugs - 
# Challenges -
#1) The game keeps score over multiple games
#2) The game allows for more than one user
#3) Multiple different user errors are addressed
#4) Option to play against the computer or another user
#5) Introduce a score limit
# Sources - https://www.python.org/, https://www.w3schools.com/python/

print("Hello! Welcome to Bill's Rock Paper Scissors!")
print('')

playerscore = 0
computerscore = 0

import random
while True:

    if (playerscore == 5 or computerscore == 5):
        print('')
        print('Game over!')
        print('')
        break
    
    weaponlist = ['rock','paper','scissors']
    computerweapon = weaponlist[random.randint(0,2)]
    userweapon = 'none'
    while userweapon not in ['rock','paper','scissors','']:
     userweapon = input("Please type Rock, Paper, Scissors, or Enter to Quit: ").lower()        
    if userweapon.lower() == '':
        print('Goodbye!')
        break
    elif computerweapon == userweapon.lower():
        print("You chose: ", userweapon)
        print("Computer chose: ", computerweapon)
        print('')
        print("Tie!")
        print('')
        playerscore += 1
        computerscore += 1
        print('Your score: ', playerscore)
        print('Compuer score: ', computerscore)
    elif (computerweapon == 'scissors' and userweapon.lower() == 'rock') or (computerweapon == 'rock' and userweapon.lower() == 'paper') or (computerweapon == 'paper' and userweapon.lower() == 'scissors'):
        print("You chose: ", userweapon)
        print("Computer chose: ", computerweapon)
        print('')
        print("You win!")
        print('')
        playerscore += 1
        print('Your score: ', playerscore)
        print('Compuer score: ', computerscore)
    else: 
        print("You chose: ", userweapon)
        print("Computer chose: ", computerweapon)
        print('')
        print("Computer wins!")
        print('')
        computerscore += 1
        print('Your score: ', playerscore)
        print('Compuer score: ', computerscore)

