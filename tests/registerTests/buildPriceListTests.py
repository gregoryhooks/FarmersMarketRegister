import unittest

from decimal import Decimal
from registerFunctions import buildPriceList


class TestBuildPriceList(unittest.TestCase):
    def setUp(self):
        pass

    # Test list creation on all products
    def testlistbuild(self):
        basket = (
            'CH1',
            'AP1',
            'CF1',
            'MK1',
            'OM1'
        )
        pricelist = buildPriceList.buildpricelist(basket)

        testlist = [
            {
                'ID': 'CH1',
                'Name': 'Chai',
                'Price': Decimal('3.11'),
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': Decimal('6.00'),
                'Discounts': {}
            },
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': Decimal('11.23'),
                'Discounts': {}
            },
            {
                'ID': 'MK1',
                'Name': 'Milk',
                'Price': Decimal('4.75'),
                'Discounts': {}
            },
            {
                'ID': 'OM1',
                'Name': 'Oatmeal',
                'Price': Decimal('3.69'),
                'Discounts': {}
            }
        ]

        self.assertListEqual(pricelist, testlist)

    # Test list creation with product that doesn't exist
    def testlistbuild2(self):
        basket = (
            'CH1',
            'AP1',
            'NOTHERE',
            'CF1',
            'MK1',
            'OM1'
        )
        pricelist = buildPriceList.buildpricelist(basket)

        testlist = [
            {
                'ID': 'CH1',
                'Name': 'Chai',
                'Price': Decimal('3.11'),
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': Decimal('6.00'),
                'Discounts': {}
            },
            -1,
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': Decimal('11.23'),
                'Discounts': {}
            },
            {
                'ID': 'MK1',
                'Name': 'Milk',
                'Price': Decimal('4.75'),
                'Discounts': {}
            },
            {
                'ID': 'OM1',
                'Name': 'Oatmeal',
                'Price': Decimal('3.69'),
                'Discounts': {}
            }
        ]

        self.assertListEqual(pricelist, testlist)


if __name__ == '__main__':
    unittest.main()
