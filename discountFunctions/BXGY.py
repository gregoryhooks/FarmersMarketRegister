#  Buy X products, Get Y products for any percentage off

#  Written by Gregory Hooks

#  Expected input:  List of items in basket, the rule to define the discount

#  Expected output: The total number of times the discount needs to be applied


# Verify that the requirements for product x is satisfied and return the appropriate number of discounts
def validate(basket, rule):
    # Get the information required to calculate the discount
    try:
        numberofx = basket.count(rule['RequiredItem'])
        numberofy = basket.count(rule['ItemToDiscount'])
        requiredx = int(rule['RequiredQuantity'])
        discountmultiplier = int(rule['NumberOfDiscounts'])
        requireditem = rule['RequiredItem']
        itemtodiscount = rule['ItemToDiscount']
        limit = int(rule['Limit'])
    except KeyError:
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0
    except ValueError:
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0

    # Validate that the rules are valid, if not, print error and return 0
    if not ((requiredx > 0) & (discountmultiplier > 0) & (limit >= 0)):
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0

    # If the basket does not meet the requirements, return 0
    if numberofx < requiredx:
        return 0

    # If the discount applies to the same item, eliminate discounted items from the list
    if requireditem == itemtodiscount:
        numberofdiscounts = 0
        while numberofx > requiredx:
            numberofdiscounts += discountmultiplier
            numberofx -= requiredx
            numberofx -= discountmultiplier
    else:
        numberofdiscounts = (numberofx / requiredx)
        numberofdiscounts *= discountmultiplier
        numberofdiscounts = min(numberofdiscounts, numberofy)

    # If there is a limit to how many times the discount can be applied, return that if discount count exceeds it
    # A limit of zero means that there is no limit
    if limit:
        return min(numberofdiscounts, limit)

    else:
        return numberofdiscounts
