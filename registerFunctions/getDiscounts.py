# Builds a list of potential discounts to the items in the basket

# Written by Gregory Hooks

# Expected input: List of items in the basket built from the build price function

# Expected output: List of discounts that reference the items in the basket

import os
import re


# Requires a price list, returns a list of discounts
def getdiscounts(basket):
    # Only use unique values in the basket to create the discount list
    basketset = set(basket)

    discountlist = {}

    # For every unique item in the basket, add all found discount rules
    for item in basketset:
        # Check if the item in the basket is valid, if not, skip it
        if item == -1:
            continue

        # Check if the defining file for the product exists, if it does, add the appropriate discount data
        discountpath = os.path.join(os.path.dirname(__file__), '../discounts/')
        discountfilelist = os.listdir(discountpath)
        r = re.compile(item)
        filteredfilelist = filter(r.match, discountfilelist)

        # If no discounts are found, move to the next item in the price list
        if len(filteredfilelist) <= 0:
            continue

        # For every discount file found for the item, add the rule
        for discountfile in filteredfilelist:
            try:
                with open(discountpath + str(discountfile), 'rb') as inputFile:
                    discountparts = {}
                    for line in inputFile:
                        name, val = line.split(":")
                        name = name.strip()
                        val = val.strip()
                        discountparts[name] = val

                    # If the product file contains to appropriate information, append the discount list
                    if ("Description" in discountparts) & ("DiscountType" in discountparts) & (
                                "RequiredItem" in discountparts) & ("PercentageOff" in discountparts) & (
                                "Combinable" in discountparts):
                        discountlist[discountfile] = discountparts
            except IOError:
                pass

    return discountlist
