import csv
from collections import defaultdict

DATA_FILE = "data.csv"
REPORT_FILE = "report.txt"

def read_data():
    sales = []
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales.append({
                "product": row["product"],
                "quantity": int(row["quantity"]),
                "price": float(row["price"])
            })
    return sales

def analyze_sales(sales):
    total_revenue = 0
    product_sales = defaultdict(int)

    for item in sales:
        revenue = item["quantity"] * item["price"]
        total_revenue += revenue
        product_sales[item["product"]] += item["quantity"]

    top_product = max(product_sales, key=product_sales.get)

    return total_revenue, product_sales, top_product

def generate_report(total, product_sales, top_product):
    with open(REPORT_FILE, "w") as file:
        file.write("=== Sales Report ===\n\n")
        file.write(f"Total Revenue: ₹{total}\n\n")

        file.write("Product Sales:\n")
        for product, qty in product_sales.items():
            file.write(f"{product}: {qty} units\n")

        file.write(f"\nTop Selling Product: {top_product}\n")

    print("Report generated successfully!")

def main():
    sales = read_data()
    total, product_sales, top_product = analyze_sales(sales)
    generate_report(total, product_sales, top_product)

if __name__ == "__main__":
    main()