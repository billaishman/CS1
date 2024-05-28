# Bill Aishman
# Food-o-Matic
# 3/1/2024
# Bugs - 
# Challenges -
#       1) Generate the costs for each of the items on the menu.
#       2) Calculate the total cost for all items.
#       3) Ensure that the user is entering a number when asking for menu items.
#       4) Remove the possibility of duplicate items (and don’t  allow the user to enter too many items).
# Sources - https://www.python.org/, https://www.w3schools.com/python/

print("Hello! Weclome to Bill's Food-O-Matic!")
print('')

import random

food = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "rainbow carrots", "potatoes", "three color squash","eggplant","eye round of beef","baguette"]
with_food = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "soup", "chutney",  "salad","with salsa","over sticky rice","au jus", "with basmati rice"]
cost = [5,6,10,2,3,4,6,8,9,1]

while True:
    sum = 0
    print('')
    items=input("How many menu items (1-10) do you need? (press enter to quit)")
    if items=="":
        print("Thank you!")
        break
    try:
        val = int(items)
    except ValueError:
            print("Please enter a number between 1 and 10.")
    else:
        items = int(items)
        if items > 10 or items < 0:
            print("Please enter a number between 1 and 10.")
        else:
            print("Here are", items, "menu items for you!")
            print('')
            randomfood = random.sample(food, items)
            randomwith_food = random.sample(with_food, items)
            randomcost=random.sample(cost, items)
            for x in range(items):
                print((x+1),") $", randomcost[x], randomfood[x], randomwith_food[x])
                sum = randomcost[x] + sum
            print("Total cost of all items:$",sum)
