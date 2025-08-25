"""
Exercise: Modify and Remove Dictionary Items

Problem:
Create a dictionary of price of fruits. The prices are:
- apple:  $8
- banana: $5
- orange: $7

Now, change the price of banana to 6, and remove the apple item. Finally, print the dictionary.
"""


def main():
    """
    Create a sample dictionary, modify the price of banana,
    Remove apple from the dictionary, and print the modified result.
    """
    fruit_prices = {
        'apple': 8,
        'banana': 5,
        'orange': 7
    }

    fruit_prices['banana'] = 6
    fruit_prices.pop('apple')
    print(fruit_prices)


if __name__ == "__main__":
    main()
