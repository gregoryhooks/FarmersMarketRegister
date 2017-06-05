import unittest

from registerFunctions import addDiscounts


class TestAddDiscount(unittest.TestCase):
    def setUp(self):
        pass

    # Test adding one discount
    def testadddisount(self):
        basket = [
            'CF1',
            'CF1'
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            }
        ]

        discountlist = {
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

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {
                    'CF1-BOGO': {
                        'PercentageOff': 100
                    }
                }
            },
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding multiple discounts on the same items
    def testadddisount2(self):
        basket = [
            'CF1',
            'AP1',
            'AP1',
            'CF1',
            'AP1',
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
        ]

        discountlist = {
            'AP1-APPL': {
                'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
                'DiscountType': 'BXGD',
                'RequiredItem': 'AP1',
                'RequiredQuantity': '3',
                'PercentageOff': '75',
                'Limit': '0',
                'Combinable': 'True'
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

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {
                    'CF1-BOGO': {
                        'PercentageOff': 100
                    }
                }
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'AP1-APPL': {
                        'PercentageOff': 75
                    }
                }
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'AP1-APPL': {
                        'PercentageOff': 75
                    }
                }
            },
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'AP1-APPL': {
                        'PercentageOff': 75
                    }
                }
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding multiple discounts that apply to the same item
    def testadddisount3(self):
        basket = [
            'CF1',
            'AP1',
            'AP1',
            'AP1',
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
        ]

        discountlist = {
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
                'Description': 'Buy one coffee, get a bag of apples free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'AP1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'CF1-BOGO': {
                        'PercentageOff': 100
                    }
                }
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding discount to a different item from requirements
    def testadddisount4(self):
        basket = [
            'CF1',
            'AP1'
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        discountlist = {
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get a bag of apples free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'AP1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'CF1-BOGO': {
                        'PercentageOff': 100
                    }
                }
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding discount with combinable discounts
    def testadddisount5(self):
        basket = [
            'CF1',
            'AP1',
            'AP1',
            'AP1'
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        discountlist = {
            'AP1-APPL': {
                'Description': 'Buy 3 or more bags of Apples, get them for $4.50 each',
                'DiscountType': 'BXGD',
                'RequiredItem': 'AP1',
                'RequiredQuantity': '3',
                'PercentageOff': '25',
                'Limit': '0',
                'Combinable': 'True'
            },
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get a bag of apples half off.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'AP1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '50',
                'Limit': '0',
                'Combinable': 'True'
            }
        }

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'CF1-BOGO': {
                        'PercentageOff': 50
                    },
                    'AP1-APPL': {
                        'PercentageOff': 25
                    }
                }
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'AP1-APPL': {
                        'PercentageOff': 25
                    }
                }
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {
                    'AP1-APPL': {
                        'PercentageOff': 25
                    }
                }
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding discount with invalid type
    def testadddisount6(self):
        basket = [
            'CF1',
            'AP1'
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        discountlist = {
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get a bag of apples free.',
                'DiscountType': 'BX',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'AP1',
                'NumberOfDiscounts': '1',
                'PercentageOff': '100',
                'Limit': '0',
                'Combinable': 'False'
            }
        }

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)

    # Test adding discount with invalid data
    def testadddisount7(self):
        basket = [
            'CF1',
            'AP1'
        ]

        pricelist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        discountlist = {
            'CF1-BOGO': {
                'Description': 'Buy one coffee, get a bag of apples free.',
                'DiscountType': 'BXGY',
                'RequiredItem': 'CF1',
                'RequiredQuantity': '1',
                'ItemToDiscount': 'AP1',
                'NumberOfDiscounts': '1',
                'PercentageOff': 'onehundred',
                'Limit': '0',
                'Combinable': 'False2'
            }
        }

        testlist = [
            {
                'ID': 'CF1',
                'Name': 'Coffee',
                'Price': '$11.23',
                'Discounts': {}
            },
            {
                'ID': 'AP1',
                'Name': 'Apples',
                'Price': '$6.00',
                'Discounts': {}
            }
        ]

        addDiscounts.add_discounts(discountlist, basket, pricelist)

        self.assertListEqual(testlist, pricelist)


if __name__ == '__main__':
    unittest.main()
