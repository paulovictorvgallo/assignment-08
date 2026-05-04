# Module 6 Assignment: Functions and Modular Programming
# TechRetail Sales Analysis System

print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data 
# Format: [product_name, category, price, quantity_sold, employee_id]
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee information
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# -----------------------------
# 1. Sales Analysis Functions
# -----------------------------

def calculate_total_sales():
    """
    Calculates the total revenue from all sales.

    Returns:
        float: The total sales revenue.
    """
    total = 0
    for product in sales_data:
        price = product[2]
        quantity = product[3]
        total += price * quantity
    return total


def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.

    Args:
        category (str): The product category to calculate sales for.

    Returns:
        float: The total sales revenue for the specified category.
    """
    total = 0
    for product in sales_data:
        if product[1] == category:
            total += product[2] * product[3]
    return total


def find_best_selling_product():
    """
    Identifies the product with the highest total revenue.

    Returns:
        tuple: (product_name, total_revenue)
    """
    best_product = ""
    highest_revenue = 0

    for product in sales_data:
        revenue = product[2] * product[3]
        if revenue > highest_revenue:
            highest_revenue = revenue
            best_product = product[0]

    return (best_product, highest_revenue)


# -----------------------------
# 2. Commission Functions
# -----------------------------

def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.

    Args:
        employee_id (str): The unique identifier of the employee.

    Returns:
        float: The commission amount earned.
    """
    total_sales = 0
    for product in sales_data:
        if product[4] == employee_id:
            total_sales += product[2] * product[3]

    commission_rate = employees[employee_id][1]
    return total_sales * commission_rate


def calculate_total_commission():
    """
    Calculates the total commission for all employees.

    Returns:
        float: Total commission payout.
    """
    total = 0
    for emp_id in employees:
        total += calculate_employee_commission(emp_id)
    return total


# -----------------------------
# 3. Report Functions
# -----------------------------

def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.

    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.

    Returns:
        str: Formatted report string.
    """
    report = "SALES SUMMARY REPORT\n"
    report += "-" * 30 + "\n"
    report += f"Total Revenue: ${calculate_total_sales():,.2f}\n"
    report += f"Average Sale Price: ${calculate_average_sale_price():,.2f}\n"

    best_product, revenue = find_best_selling_product()
    report += f"Best-Selling Product: {best_product} (${revenue:,.2f})\n"

    if include_categories:
        report += "\nRevenue by Category:\n"
        categories = set([product[1] for product in sales_data])
        for category in categories:
            category_total = calculate_category_sales(category)
            report += f"- {category}: ${category_total:,.2f}\n"

    return report


def generate_employee_report():
    """
    Generates a formatted employee performance report.

    Returns:
        str: Employee performance report.
    """
    report = "EMPLOYEE PERFORMANCE REPORT\n"
    report += "-" * 30 + "\n"

    for emp_id, info in employees.items():
        name = info[0]
        total_sales = 0
        for product in sales_data:
            if product[4] == emp_id:
                total_sales += product[2] * product[3]

        commission = calculate_employee_commission(emp_id)

        report += f"{name}\n"
        report += f"  Total Sales: ${total_sales:,.2f}\n"
        report += f"  Commission Earned: ${commission:,.2f}\n\n"

    report += f"Total Commission Payout: ${calculate_total_commission():,.2f}\n"
    return report


# -----------------------------
# 4. Utility Functions
# -----------------------------

def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.

    Args:
        category (str): The product category to filter by.

    Returns:
        list: List of product names in the specified category.
    """
    products = []
    for product in sales_data:
        if product[1] == category:
            products.append(product[0])
    return products


def calculate_average_sale_price():
    """
    Calculates the average sale price across all transactions.

    Returns:
        float: Average sale price.
    """
    total_revenue = calculate_total_sales()
    total_units = sum(product[3] for product in sales_data)
    return total_revenue / total_units


# -----------------------------
# 5. Main Program
# -----------------------------

def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)

    print("\nTOTAL QUARTERLY SALES:")
    total_sales = calculate_total_sales()
    print(f"${total_sales:,.2f}")

    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for category in categories:
        print(f"{category}: ${calculate_category_sales(category):,.2f}")

    print("\nBEST-SELLING PRODUCT:")
    product, revenue = find_best_selling_product()
    print(f"{product} - ${revenue:,.2f}")

    print("\nEMPLOYEE COMMISSIONS:")
    for emp_id, info in employees.items():
        name = info[0]
        commission = calculate_employee_commission(emp_id)
        print(f"{name}: ${commission:,.2f}")

    print("\nQUARTERLY SALES SUMMARY REPORT:")
    print(generate_sales_summary())

    print("\nEMPLOYEE PERFORMANCE REPORT:")
    print(generate_employee_report())


if __name__ == "__main__":
    main()