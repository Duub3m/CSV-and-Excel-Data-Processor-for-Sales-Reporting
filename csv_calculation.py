import csv

# Path to the input CSV file
input_file = 'products.csv'  # name of the CSV file.
output_file = 'products_with_total.csv'  # new CSV file.

# Opens the CSV file, reads the data, and calculates total revenue
with open(input_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    products = []
    
    # Adds a new field for total revenue
    for row in csv_reader:
        product = row['Product']
        quantity = int(row['Quantity'])
        price = float(row['Price'])
        total = quantity * price
        products.append({'Product': product, 'Quantity': quantity, 'Price': price, 'Total Revenue': total})

# Writes the updated data with the total revenue back to a new CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = ['Product', 'Quantity', 'Price', 'Total Revenue']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(products)

print(f"File '{output_file}' has been created with the total revenue column.")
