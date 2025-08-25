"""
Exercise: Special Discount Calculation

Problem:
A store offers special discounts based on the purchase amount:
- If the purchase amount is greater than $50, a 20% discount is applied.
- If the purchase amount is between $20 and $50, a 10% discount is applied.
- If the purchase amount is less than $20, no discount is applied.

The program should calculate the final amount after applying the discount.

Input:
A single float representing the purchase amount in USD.

Output:
The final purchase amount in USD after applying the discount.
"""


def calculate_final_price(price_before_discount):
    """Calculate the final price after applying the discount based on the rules."""
    if price_before_discount > 50:
        discount = 0.2  # 20% discount
        final_price = price_before_discount - discount * price_before_discount
    elif 20 <= price_before_discount <= 50:
        discount = 0.1  # 10% discount
        final_price = price_before_discount - discount * price_before_discount
    else:
        final_price = price_before_discount  # No discount

    return final_price


def main():
    """
    Calculates and displays the final price after a discount.

    This function serves as the script's entry point. It prompts the user
    to enter a purchase amount, passes this amount to a helper function
    to calculate the applicable discount, and then prints the final,
    discounted price formatted to two decimal places.
    """
    # Get user input (purchase amount in USD)
    price_before_discount = float(input("Enter the purchase amount in USD: "))

    # Calculate the final price
    final_price = calculate_final_price(price_before_discount)

    # Print the final price
    print(f"The final price after discount is ${final_price:.2f}")


if __name__ == "__main__":
    main()
