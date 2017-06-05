# Buy X Products, get them all at any percentage off

#  Written by Gregory Hooks

#  Expected input:  List of items in basket, the rule to define the discount

#  Expected output: The total number of times the discount needs to be applied

# Verify that the requirements for product x is satisfied and return the appropriate number of discounts
def validate(basket, rule):
    # Get the information required to calculate the discount
    try:
        numberofx = basket.count(rule['RequiredItem'])
        requiredx = int(rule['RequiredQuantity'])
        limit = int(rule['Limit'])
    except (KeyError):
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0
    except ValueError:
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0

    # Validate that the rules are valid, if not, print error and return 0
    if not ((requiredx > 0) & (limit >= 0)):
        print "Warning:  Ignoring invalid discount \"" + rule['Description'] + "\""
        return 0

    # If the requirement is satisfied, return the number of items as the amount to discount or the limit
    if numberofx >= requiredx:
        if limit:
            return min(numberofx, limit)
        else:
            return numberofx
    else:
        return 0
