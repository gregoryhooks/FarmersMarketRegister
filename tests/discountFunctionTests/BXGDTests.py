import unittest

from discountFunctions import BXGD


class TestBXGD(unittest.TestCase):
    def setUp(self):
        pass

    # Test with invalid data
    def testinvaliddiscount1(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
            'DiscountType': 'BXGD',
            'RequiredItem': 'AP1',
            'RequiredQuantity': 'three',
            'PercentageOff': 'seventy-five',
            'Limit': 'zero',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with missing data
    def testinvaliddiscount2(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
            'DiscountType': 'BXGD',
            'PercentageOff': '75',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with invalid values
    def testinvaliddiscount3(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
            'DiscountType': 'BXGD',
            'RequiredItem': 'AP1',
            'RequiredQuantity': '-1',
            'PercentageOff': '75',
            'Limit': '-1',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with requirements not satisfied
    def testdiscount1(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
            'DiscountType': 'BXGD',
            'RequiredItem': 'AP1',
            'RequiredQuantity': '3',
            'PercentageOff': '75',
            'Limit': '0',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 0, "Expected number of discounts is 0")

    # Test with requirements satisfied
    def testdiscount2(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
            'DiscountType': 'BXGD',
            'RequiredItem': 'AP1',
            'RequiredQuantity': '3',
            'PercentageOff': '75',
            'Limit': '0',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 3, "Expected number of discounts is 3")

    # Test with requirements satisfied with limit
    def testdiscount3(self):
        rule = {
            'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each.  Limit 6.',
            'DiscountType': 'BXGD',
            'RequiredItem': 'AP1',
            'RequiredQuantity': '3',
            'PercentageOff': '75',
            'Limit': '6',
            'Combinable': 'True'
        }

        basket = (
            'CF1',
            'CF1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'AP1',
            'CH1'
        )

        number = BXGD.validate(basket, rule)
        self.assertEqual(number, 6, "Expected number of discounts is 6")


if __name__ == '__main__':
    unittest.main()
