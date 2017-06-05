#  Adds the appropriate discounts to the price list

#  Written by Gregory Hooks

#  Expected input:  List of discounts, list of items in basket, the price list to add the discounts to

#  Expected side effect: Modifies the price list parameter!

#  !!! The functions imported here are used in an eval statement, do not remove !!!
from discountFunctions import *


# Directly adds discounts to the pricelist
def add_discounts(discountlist, basket, pricelist):
    # This list will hold the available discounts for each item
    discounttally = {}

    # For every discount in the discountlist, group them by item
    for discount, value in discountlist.items():
        discounttype = value["DiscountType"]
        # Verify that the rule exists, if not, move to the next discount
        try:
            discountnumber = eval(discounttype + ".validate(basket, value)")
        except NameError:
            continue
        if "ItemToDiscount" in value:
            discountitem = value['ItemToDiscount']
        else:
            discountitem = value['RequiredItem']
        if discountnumber > 0:
            try:
                percent = int(value['PercentageOff'])
                if value['Combinable'] == "True":
                    combinable = True
                elif value['Combinable'] == "False":
                    combinable = False
                else:
                    continue
            except ValueError:
                continue
            if discountitem not in discounttally:
                discounttally[discountitem] = []
            discounttally[discountitem].append({
                'ID': discount,
                'Count': discountnumber,
                'Combinable': combinable,
                'PercentageOff': percent
            })

    # Sort the discounts into 2 groups.  Combinable and non-combinable.
    # Runs a tally of the total savings offered by all combinable and each non-combinable discount.
    # Only the discount(s) with the best total savings is selected
    for item, value in discounttally.iteritems():
        if len(value) > 1:
            combinablediscounts = []
            combinetotal = 0
            notcombinabledicounts = []
            notcombinelist = []
            for discount in value:
                count = discount['Count']
                percent = discount['PercentageOff']
                combinable = discount['Combinable']
                if combinable:
                    combinablediscounts.append(discount)
                    combinetotal += count * percent
                else:
                    notcombinabledicounts.append(discount)
                    notcombinelist.append(count * percent)
            if len(notcombinelist) < 1:
                discounttally[item] = combinablediscounts
            elif combinetotal > max(notcombinelist):
                discounttally[item] = combinablediscounts
            else:
                maxindex = notcombinelist.index(max(notcombinelist))
                discounttally[item] = [notcombinabledicounts[maxindex]]

    # Inserts the selected discount(s) into the appropriate items in the basket
    for item in pricelist:
        if item['ID'] in discounttally:
            if len(discounttally[item['ID']]):
                for i, discount in enumerate(discounttally[item['ID']]):
                    # If the discount apply limit hasn't been reached, apply it
                    if discount['Count'] > 0:
                        item['Discounts'][discount['ID']] = {
                            'PercentageOff': int(discount['PercentageOff'])
                        }
                        # Decrement the counter for the number of times the discount is valid
                        discount['Count'] -= 1
