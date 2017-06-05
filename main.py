#  Driver program for Farmer's Market Register

#  Written by Gregory Hooks

from registerFunctions import *
import os


# Customize a clear screen function for windows or unix
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()
programboolean = True

# Loops until the user is finished tallying up baskets
while programboolean:
    basket = []

    # Loops until the user enters an empty string to signal for the final tally
    while True:
        print "When you are finished adding items to the tally, leave the line blank and press enter"
        item = raw_input('Item product code: ')
        clear()
        item = item.strip()

        # If the user enters an empty string, print the final total if the basket has items in it
        if not item:
            if len(basket) > 0:
                clear()
                print "Final Total for Basket"
                discountlist = getDiscounts.getdiscounts(basket)
                addDiscounts.add_discounts(discountlist, basket, pricelist)
                printOutput.printregisteroutput(pricelist)
            break

        # Insert item in the basket
        basket.append(item)

        # Build a pricelist from the items in the basket
        pricelist = buildPriceList.buildpricelist(basket)

        # If the item entered is not found, remove it from the basket and pricelist
        if pricelist[-1] == -1:
            print item + " is not a valid product code"
            del basket[-1]
            del pricelist[-1]

        # Get all potential discounts for the items in the basket
        discountlist = getDiscounts.getdiscounts(basket)

        # Add the appropriate discounts to the items in the basket
        addDiscounts.add_discounts(discountlist, basket, pricelist)

        # Output the formatted tally to the screen
        printOutput.printregisteroutput(pricelist)

    # Loops until the user confirms or denies that they want to start input on a new basket
    while True:
        newanswer = raw_input('Would you like to input a new basket? (y/n)')
        if newanswer == "y":
            clear()
            break
        elif newanswer == "n":
            programboolean = False
            break
