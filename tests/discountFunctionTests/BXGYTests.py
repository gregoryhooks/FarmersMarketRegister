import unittest

from discountFunctions import BXGY


class TestBXGY(unittest.TestCase):
    def setUp(self):
        pass

    # Test with invalid data
    def testinvaliddiscount1(self):
        rule = {
            'Description': 'Buy one coffee, get another free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': 'one',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': 'one',
            'Limit': 'one',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with missing data
    def testinvaliddiscount2(self):
        rule = {
            'Description': 'Buy one coffee, get another free.',
            'DiscountType': 'BXGY',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with invalid required quantity, discounts, and limit
    def testinvaliddiscount3(self):
        rule = {
            'Description': 'Buy one coffee, get another free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '-1',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': '-1',
            'Limit': '-1',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with one discount of same item
    def testselfdiscount1(self):
        rule = {
            'Description': 'Buy one coffee, get another free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '1',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': '1',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 1, "Expected number of discounts is 1")

    # Test with requirements of one discount of same item
    def testselfdiscount2(self):
        rule = {
            'Description': 'Buy 3 coffees, get another free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '3',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': '1',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 2, "Expected number of discounts is 2")

    # Test with requirements of one discount of same item with limit
    def testselfdiscount3(self):
        rule = {
            'Description': 'Buy 3 coffees, get another free.  Limit 1.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '3',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': '1',
            'Limit': '1',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 1, "Expected number of discounts is 1")

    # Test with requirements and more than one discounted item
    def testselfdiscount4(self):
        rule = {
            'Description': 'Buy 3 coffees, get another 2 free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '3',
            'ItemToDiscount': 'CF1',
            'NumberOfDiscounts': '2',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'CH1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 4, "Expected number of discounts is 4")

    # Test with multiple discounts with different items
    def testdiscount1(self):
        rule = {
            'Description': 'Buy one coffee, get a bag of apples free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '1',
            'ItemToDiscount': 'AP1',
            'NumberOfDiscounts': '1',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 1, "Expected number of discounts is 1")

    # Test with required items with different items
    def testdiscount2(self):
        rule = {
            'Description': 'Buy 2 coffees, get a bag of apples free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '2',
            'ItemToDiscount': 'AP1',
            'NumberOfDiscounts': '1',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 2, "Expected number of discounts is 2")

    # Test with multiple discounts with different items and a limit
    def testdiscount3(self):
        rule = {
            'Description': 'Buy one coffee, get a bag of apples free.  Limit 2.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '1',
            'ItemToDiscount': 'AP1',
            'NumberOfDiscounts': '1',
            'Limit': '2',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 2, "Expected number of discounts is 2")

    # Test with required items with multiple different items
    def testdiscount4(self):
        rule = {
            'Description': 'Buy 2 coffees, get 3 bags of apples free.',
            'DiscountType': 'BXGY',
            'RequiredItem': 'CF1',
            'RequiredQuantity': '2',
            'ItemToDiscount': 'AP1',
            'NumberOfDiscounts': '3',
            'Limit': '0',
            'PercentageOff': '100',
            'Combinable': 'False'
        }

        basket = (
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'CH1',
            'CF1',
            'CF1'
        )

        number = BXGY.validate(basket, rule)
        self.assertEqual(number, 4, "Expected number of discounts is 4")


if __name__ == '__main__':
    unittest.main()
