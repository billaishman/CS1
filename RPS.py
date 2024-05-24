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

import random

#Below here is the code for 2-Player Mode
def two_player():
        print("Two Player Mode:")
        print('')
        playeronescore = 0
        playertwoscore = 0        
#this makes the score go up to five and then ends the game 
        while True:
            if (playeronescore == 5 or playertwoscore == 5):
                print('')
                print('Game over!')
                print('')
                break

            oneweapon = 'none'
            while oneweapon not in ['rock','paper','scissors','']:
             oneweapon = input("Player one: Please type Rock, Paper, Scissors, or Enter to Quit: ").lower()  
            twoweapon = 'none'
            while twoweapon not in ['rock','paper','scissors','']:
             twoweapon = input("Player two: Please type Rock, Paper, Scissors, or Enter to Quit: ").lower()        
            if oneweapon.lower() == '' or twoweapon.lower() == '':
                print('Goodbye!')
                break
            elif oneweapon == twoweapon.lower():
                print("Player one chose: ", oneweapon)
                print("Player two chose: ", twoweapon)
                print('')
                print("Tie!")
                print('')
                playeronescore += 1
                playertwoscore += 1
                print('Player one score: ', playeronescore)
                print('Player two score: ', playertwoscore)
            elif (twoweapon == 'scissors' and oneweapon == 'rock') or (twoweapon == 'rock' and oneweapon == 'paper') or (twoweapon == 'paper' and oneweapon == 'scissors'):
                print("Player one chose: ", oneweapon)
                print("Player two chose: ", twoweapon)
                print('')
                print("Player One wins!")
                print('')
                playeronescore += 1
                print('Player one score: ', playeronescore)
                print('Player two score: ', playertwoscore)
            else: 
                print("Player one chose: ", oneweapon)
                print("Player two chose: ", twoweapon)
                print('')
                print("Player Two wins!")
                print('')
                playertwoscore += 1
                print('Player one score: ', playeronescore)
                print('Player two score: ', playertwoscore)

#Below here is the code for Computer Mode
def computer_mode():
    print("Computer Mode:")
    print('')

    playerscore = 0
    computerscore = 0

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

#This is where the choice is made!
print("Hello! Welcome to Bill's Rock Paper Scissors!")
print('Rules: Rock>Scissors,Paper>Rock,Scissors>Paper. First to 5 Wins!')
print('')
gamechoice = 'none'
while gamechoice not in ['1','2']:
    gamechoice = input("Type 1 for Computer Mode. Type 2 for 2 Player Mode: ")
if gamechoice == '2':
    two_player()
else:
    computer_mode()
    
