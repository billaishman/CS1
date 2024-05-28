# Bill Aishman
# Magic 8-ball
# 11/9/2023
# Bugs - 
# Challenges - 
# Sources - https://www.python.org/, https://www.w3schools.com/python/

print("Hello! Weclome to Bill's Magic 8-Ball!")
print('')
answers = ['Yes!','No.','Maybe...','Ask again later ...']

import random
while True:
    question=input("Ask the magic 8 ball a question: (press enter to quit) ")
    if question=="":
        print("Thanks for playing!")
        break
    else:
        print(answers[random.randint(0,3)])
