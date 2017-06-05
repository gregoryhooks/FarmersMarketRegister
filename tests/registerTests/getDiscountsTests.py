import unittest

from registerFunctions import getDiscounts


class TestGetDiscount(unittest.TestCase):
    def setUp(self):
        pass

    # Test building list of all potential discounts with an invalid item in the basket
    def testgetdisountwithinvalid(self):
        basket = [
            'AP1',
            'CF1',
            'NOTHERE'
        ]

        testlist = {
            'AP1-APPL': {
                'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
                'DiscountType': 'BXGD',
                'RequiredItem': 'AP1',
                'RequiredQuantity': '3',
                'PercentageOff': '25',
                'Limit': '0',
                'Combinable': 'False'
            },
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get another free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'CF1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        discountlist = getDiscounts.getdiscounts(basket)

        self.assertDictEqual(testlist, discountlist)

    # Test building list of all potential discounts
    def testgetdisount(self):
        basket = [
            'AP1',
            'CF1'
        ]

        testlist = {
            'AP1-APPL': {
                'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
                'DiscountType': 'BXGD',
                'RequiredItem': 'AP1',
                'RequiredQuantity': '3',
                'PercentageOff': '25',
                'Limit': '0',
                'Combinable': 'False'
            },
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get another free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'CF1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        discountlist = getDiscounts.getdiscounts(basket)

        self.assertDictEqual(testlist, discountlist)

    # Test building list of all potential discounts with duplicate items in basket
    def testgetdisount2(self):
        basket = [
            'AP1',
            'AP1',
            'AP1',
            'CF1',
            'CF1'
        ]

        testlist = {
            'AP1-APPL': {
                'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
                'DiscountType': 'BXGD',
                'RequiredItem': 'AP1',
                'RequiredQuantity': '3',
                'PercentageOff': '25',
                'Limit': '0',
                'Combinable': 'False'
            },
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get another free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'CF1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        discountlist = getDiscounts.getdiscounts(basket)

        self.assertDictEqual(testlist, discountlist)


if __name__ == '__main__':
    unittest.main()
