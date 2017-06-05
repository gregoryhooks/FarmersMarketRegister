# Farmer's Market Register

Written for Python 2.7

## Usage:

```
python ./main.py
```

## Configuration

This program includes 5 products and 4 discounts.

### Adding Products

The filename for each product must match the desired product code e.g. "AP1".

Below is the format for a product, all fields are **required**:

```
Name: Specifies the full name of the product e.g. "Apples"
Price: Specifies the dollar amount of the product e.g. "$6.00"
```

### Adding Discounts
The filename for each discount has a specific format.

The filename should start with the product code for the conditional item that is needed in order for the discount to apply to.

Then a "-" is to be used to separate the product code from the discount code.

The discount code is arbitrary, use whatever is suitable here.

Below is an example of a discount filename:

```
OM1-APOM
```

"OM1" since the condition for this discount is X amount of Oatmeal.

"APOM" in this example means you get a discount on apples if you buy x amount of Oatmeal, again this name is arbitrary.

Below is the **minimal** format for the discount file itself:

```
Description: Helps identify what the discount is in human readable terms
DiscountType: Defines which rule calculates how this discount is applied, more information below
RequiredItem: Should match the beginning of the filename and defines what item is needed in order for the discount to become effective
RequiredQuantity: Defines how many of the required item is needed in order for this discount to become effective
PercentageOff: Defines how much the discount (if applicable) will deduct from the original price
Limit: Limits how many times the discount can be applied
Combinable: Defines whether or not this discount can be combined with another discount.  The discount(s) with the highest overall savings will be chosen.
```

### Discount Rules

There are 2 discount rules included.

#### BXGY

*"Buy X amount of items, get Y amount of items at any percentage off."*

In addition to the minimal format above, this rule **requires** the following attributes:

```
ItemToDiscount: The item which the discount will apply to
NumberOfDiscounts: The number of the items the discount will apply to
```

#### BXGD

*"Buy X amount of items, get them all for any percentage off."*

This rule does not require any additional fields.
