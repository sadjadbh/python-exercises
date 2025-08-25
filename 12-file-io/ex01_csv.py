"""
Exercise: Working with CSV Files

Problem:
Read a CSV file containing product names, prices, and quantities.
Calculate the total price (price × quantity) for each product and write the results
to a new CSV file with an additional "Total Price" column.

Input:
CSV file format:
Product,Price,Quantity

Output:
CSV file format:
Product,Price,Quantity,Total Price
"""

import csv


def process_csv(input_file: str, output_file: str) -> None:
    """
    Read input CSV, calculate total price for each product, and save results to output CSV.
    """
    with open(input_file, mode='r', encoding='utf-8', newline='') as i_file:
        reader = csv.DictReader(i_file)
        fieldnames = reader.fieldnames + ['Total Price']

        processed_data = []
        for row in reader:
            try:
                price = float(row['Price'])
                quantity = float(row['Quantity'])
                row['Total Price'] = price * quantity
            except (ValueError, KeyError):
                row['Total Price'] = 'Invalid data'
            processed_data.append(row)

    with open(output_file, mode='w', encoding='utf-8', newline='') as o_file:
        writer = csv.DictWriter(o_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)


def main():
    """
    Main function to execute the CSV processing task.
    """
    process_csv('input.csv', 'output.csv')
    print("Processing complete! Results saved to output.csv")


if __name__ == "__main__":
    main()
