#  Outputs items in the basket with prices and discounts

#  Written by Gregory Hooks

#  Expected input:  Price list object with discounts applied as needed

from decimal import Decimal


# Prints a formatted output of the price list for human reading
def printregisteroutput(pricelist):
    totalprice = Decimal('0.00')
    print '{:17s} {:>17s}'.format("Item", "Price")
    print '{:17s} {:>17s}'.format("----", "-----")

    # For every item in the price list, add its price to the total,
    # print all discounts and deduct them from the total price
    for item in pricelist:
        totalprice += item['Price']
        print '{:17s} {:>17s}'.format(item['ID'], str(item['Price']))
        for discount, value in item['Discounts'].items():
            percentage = Decimal(value['PercentageOff']) / 100
            discountoff = item['Price'] * percentage
            discountoff = discountoff.quantize(Decimal(10) ** -2)
            discountoff *= -1
            totalprice += discountoff
            print '{:>17s} {:>17s}'.format(discount.split('-')[1], str(discountoff))

    print "-----------------------------------"
    print str(totalprice).rjust(35)
