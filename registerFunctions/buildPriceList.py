# Build a data structure that gives the initial price for each item in the basket

# Written by Gregory Hooks

# Expected input: List of items in the basket

# Expected output:  A list containing a dictionary for each item, or -1 if it doesn't exist


from decimal import Decimal
import os


# Build the price list data structure and return it
def buildpricelist(basket):
    pricelist = []
    for item in basket:
        # Check if the defining file for the product exists, if it does, create the dictionary and append to the price list
        productpath = os.path.join(os.path.dirname(__file__), '../products/' + item)
        try:
            with open(productpath, 'rb') as inputFile:
                itemparts = {'ID': item}
                itemparts["Discounts"] = {}
                for line in inputFile:
                    name, val = line.split(":")
                    name = name.strip()
                    val = val.strip()
                    itemparts[name] = val

                # If the product file does not contain to appropriate information, append -1
                if ("Name" in itemparts) & ("Price" in itemparts):
                    itemparts['Price'] = Decimal(itemparts['Price'].strip("$"))
                    pricelist.append(itemparts)
                else:
                    pricelist.append(-1)
        except (IOError):
            pricelist.append(-1)
    return pricelist
